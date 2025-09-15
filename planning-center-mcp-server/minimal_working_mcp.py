#!/usr/bin/env python3
"""Minimal working MCP server to test the correct pattern."""

import asyncio
import sys
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Create a minimal server
server = Server("minimal-test")


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    print("list_tools() called", file=sys.stderr)
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
    print(
        f"call_tool() called with name: {name}, arguments: {arguments}", file=sys.stderr
    )
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

            # Create initialization options
            init_options = server.create_initialization_options()
            print(f"Initialization options created: {init_options}", file=sys.stderr)

            print("Starting server.run()...", file=sys.stderr)
            await server.run(
                read_stream,
                write_stream,
                init_options,
            )
            print("Server.run() completed successfully", file=sys.stderr)

    except Exception as e:
        print(f"Error running MCP server: {e}", file=sys.stderr)
        import traceback

        print(f"Traceback: {traceback.format_exc()}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
