from langchain_community.tools import DuckDuckGoSearchRun
from fastmcp import FastMCP

mcp = FastMCP(name='Demo Server')

@mcp.tool
def search_online_tool(query: str):
    """Search the web."""
    response =  DuckDuckGoSearchRun().invoke(query)
    return response

if __name__ == "__main__":
    mcp.run(transport= "http", host= "0.0.0.0", port=8000)