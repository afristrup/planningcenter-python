#!/usr/bin/env python3
"""Minimal MCP server test to understand the correct initialization pattern."""

import asyncio
import sys
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import InitializationOptions, Tool, TextContent

# Create a minimal server
server = Server("test-server")


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="test_tool",
            description="A simple test tool",
            inputSchema={
                "type": "object",
                "properties": {
                    "message": {"type": "string", "description": "A test message"}
                },
                "required": ["message"],
            },
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls."""
    if name == "test_tool":
        message = arguments.get("message", "Hello")
        return [TextContent(type="text", text=f"Test tool response: {message}")]
    else:
        raise ValueError(f"Unknown tool: {name}")


async def main():
    """Run the minimal MCP server."""
    print("Starting minimal MCP server...", file=sys.stderr)

    try:
        async with stdio_server() as (read_stream, write_stream):
            print("MCP server transport established", file=sys.stderr)

            # Try different initialization patterns
            try:
                # Pattern 1: No capabilities
                await server.run(
                    read_stream,
                    write_stream,
                    InitializationOptions(
                        server_name="test-server",
                        server_version="0.1.0",
                    ),
                )
            except Exception as e1:
                print(f"Pattern 1 failed: {e1}", file=sys.stderr)

                try:
                    # Pattern 2: With capabilities but None values
                    await server.run(
                        read_stream,
                        write_stream,
                        InitializationOptions(
                            server_name="test-server",
                            server_version="0.1.0",
                            capabilities=server.get_capabilities(
                                notification_options=None,
                                experimental_capabilities=None,
                            ),
                        ),
                    )
                except Exception as e2:
                    print(f"Pattern 2 failed: {e2}", file=sys.stderr)

                    # Pattern 3: With empty dict for experimental_capabilities
                    await server.run(
                        read_stream,
                        write_stream,
                        InitializationOptions(
                            server_name="test-server",
                            server_version="0.1.0",
                            capabilities=server.get_capabilities(
                                notification_options=None,
                                experimental_capabilities={},
                            ),
                        ),
                    )

    except Exception as e:
        print(f"Error running MCP server: {e}", file=sys.stderr)
        import traceback

        print(f"Traceback: {traceback.format_exc()}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
