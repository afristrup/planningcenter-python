#!/usr/bin/env python3
"""Test script to run all tests for the Planning Center API wrapper."""

import subprocess
import sys
from pathlib import Path


def run_command(command: list[str], description: str) -> bool:
    """Run a command and return success status."""
    print(f"\n{'=' * 60}")
    print(f"Running: {description}")
    print(f"Command: {' '.join(command)}")
    print("=" * 60)

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        print(f"✅ {description} - PASSED")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - FAILED")
        print(f"Return code: {e.returncode}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        return False


def main():
    """Run all tests and checks."""
    print("🧪 Planning Center API Wrapper - Comprehensive Test Suite")
    print("=" * 60)

    # Change to the planning-center-api directory
    api_dir = Path(__file__).parent / "planning-center-api"
    if not api_dir.exists():
        print(f"❌ Directory not found: {api_dir}")
        sys.exit(1)

    # List of tests to run
    tests = [
        # Linting
        (["python", "-m", "ruff", "check", "."], "Ruff Linting"),
        (["python", "-m", "black", "--check", "."], "Black Formatting Check"),
        (["python", "-m", "isort", "--check-only", "."], "Import Sorting Check"),
        (["python", "-m", "mypy", "."], "Type Checking"),
        # Unit Tests
        (["python", "-m", "pytest", "tests/unit/", "-v"], "Unit Tests"),
        # Integration Tests
        (["python", "-m", "pytest", "tests/integration/", "-v"], "Integration Tests"),
        # All Tests with Coverage
        (
            [
                "python",
                "-m",
                "pytest",
                "tests/",
                "--cov=planning_center_api",
                "--cov-report=term-missing",
                "-v",
            ],
            "All Tests with Coverage",
        ),
    ]

    # Run tests
    passed = 0
    failed = 0

    for command, description in tests:
        if run_command(command, description):
            passed += 1
        else:
            failed += 1

    # Summary
    print(f"\n{'=' * 60}")
    print("📊 TEST SUMMARY")
    print("=" * 60)
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"📈 Total: {passed + failed}")

    if failed == 0:
        print("\n🎉 All tests passed! The Planning Center API wrapper is ready.")
        return 0
    else:
        print(f"\n⚠️  {failed} test(s) failed. Please review the output above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
