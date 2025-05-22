from mcp.server.fastmcp import FastMCP
from tools import register_tools
from resources import register_resources

# Initialize FastMCP server
mcp = FastMCP("fhir")

# Register tools
register_tools(mcp)
register_resources(mcp)

if __name__ == "__main__":
    mcp.run(transport='stdio')
