from langchain_community.tools import DuckDuckGoSearchRun

from agents import function_tool


# @function_tool
def search_online_tool(query: str):
    """Search the web."""
    response =  DuckDuckGoSearchRun().invoke(query)
    return response
