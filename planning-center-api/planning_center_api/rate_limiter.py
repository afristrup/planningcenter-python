"""Rate limiting for Planning Center API."""

import asyncio
import time
from dataclasses import dataclass


@dataclass
class RateLimitInfo:
    """Information about rate limiting."""

    requests_remaining: int
    reset_time: float
    retry_after: int | None = None


class PCORateLimiter:
    """Rate limiter for Planning Center API requests."""

    def __init__(
        self,
        max_requests: int = 100,
        window_seconds: int = 60,
        backoff_factor: float = 2.0,
        max_retries: int = 3,
    ):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.backoff_factor = backoff_factor
        self.max_retries = max_retries

        self.requests: dict[float, int] = {}  # timestamp -> count
        self.lock = asyncio.Lock()

    async def acquire(self) -> None:
        """Acquire permission to make a request."""
        async with self.lock:
            now = time.time()

            # Clean up old entries
            cutoff = now - self.window_seconds
            self.requests = {
                ts: count for ts, count in self.requests.items() if ts > cutoff
            }

            # Count current requests in window
            current_requests = sum(self.requests.values())

            if current_requests >= self.max_requests:
                # Calculate wait time
                oldest_request = min(self.requests.keys())
                wait_time = self.window_seconds - (now - oldest_request)

                if wait_time > 0:
                    await asyncio.sleep(wait_time)
                    # Clean up again after waiting
                    now = time.time()
                    cutoff = now - self.window_seconds
                    self.requests = {
                        ts: count for ts, count in self.requests.items() if ts > cutoff
                    }

            # Record this request
            self.requests[now] = self.requests.get(now, 0) + 1

    async def handle_rate_limit_error(self, retry_after: int | None = None) -> None:
        """Handle a rate limit error by waiting."""
        if retry_after:
            await asyncio.sleep(retry_after)
        else:
            # Exponential backoff
            for attempt in range(self.max_retries):
                wait_time = self.backoff_factor**attempt
                await asyncio.sleep(wait_time)

    def get_rate_limit_info(self) -> RateLimitInfo:
        """Get current rate limit information."""
        now = time.time()
        cutoff = now - self.window_seconds

        # Clean up old entries
        self.requests = {
            ts: count for ts, count in self.requests.items() if ts > cutoff
        }

        current_requests = sum(self.requests.values())
        requests_remaining = max(0, self.max_requests - current_requests)

        # Calculate reset time
        if self.requests:
            oldest_request = min(self.requests.keys())
            reset_time = oldest_request + self.window_seconds
        else:
            reset_time = now

        return RateLimitInfo(
            requests_remaining=requests_remaining,
            reset_time=reset_time,
        )
