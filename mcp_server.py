from mcp.server.fastmcp import FastMCP 
from src.job_api import fetch_linkedin_jobs, fetch_indeed_jobs 

mcp = FastMCP("Job Recommender")

@mcp.tool()
async def fetchlinkedin(listofkey):
    return fetch_linkedin_jobs(listofkey)

@mcp.tool()
async def fetchindeed(listofkey):
    return fetch_indeed_jobs(listofkey)


if __name__ == "__main__":
    mcp.run(transport='stdio')