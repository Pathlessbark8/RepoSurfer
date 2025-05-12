# mcp_server.py
import argparse
import os
from pathlib import Path
from typing import List
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("FilesystemServer")

# Default root directory to serve
ROOT_DIR = Path(__file__).parent.resolve()


@mcp.tool()
def list_files(relative_path: str = "context_docs") -> List[str]:
    """
    List files and directories under ROOT_DIR/relative_path. Pass empty string to list root.
    """
    path = (ROOT_DIR / relative_path).resolve()
    if not str(path).startswith(str(ROOT_DIR)):
        return [f"Access denied: {relative_path}"]
    if not path.exists() or not path.is_dir():
        return [f"Not a directory: {relative_path}"]
    return os.listdir(path)

@mcp.tool()
def read_file(relative_path: str) -> str:
    """
    Read and return the contents of the file at ROOT_DIR/relative_path.
    """
    path = (ROOT_DIR / relative_path).resolve()
    if not str(path).startswith(str(ROOT_DIR)):
        return f"Access denied: {relative_path}"
    if not path.exists() or not path.is_file():
        return f"Not a file: {relative_path}"
    return path.read_text()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Filesystem Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse"],
        help="Transport mode (stdio or sse)",
    )
    args = parser.parse_args()

    # Start the MCP server
    mcp.run(transport=args.transport)
