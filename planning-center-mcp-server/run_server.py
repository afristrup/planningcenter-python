#!/usr/bin/env python3
"""Convenience script to run the Planning Center MCP Server."""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from planning_center_mcp.server import main

if __name__ == "__main__":
    main()
