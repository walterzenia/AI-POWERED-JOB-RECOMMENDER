from apify_client import ApifyClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
APIFY_API_KEY = os.getenv("APIFY_API_KEY")
apify_client = ApifyClient(APIFY_API_KEY)


# Fetch jobs from LinkedIn using user's search query
def fetch_linkedin_jobs(search_query="United Kingdom", rows=80):
    run_input = {
        "title": search_query,
        "location": "United Kingdom",
        "sortby": "relevance",
        "jobtype": "all",
        "remote": "all",
        "experience": "all",
        "education": "all",
        "company": "all",
        "rows": rows,
        "proxy": {
            "useApifyProxy": True,
            "apifyProxyGroups": ["RESIDENTIAL"],
        },
    }

    run = apify_client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)
    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs


# Fetch jobs from Indeed using user's search query
def fetch_indeed_jobs(search_query="sales", location="New York, NY", count=10):
    # Construct the search URL dynamically
    formatted_location = location.replace(" ", "+").replace(",", "%2C")
    search_url = f"https://www.indeed.com/jobs?q={search_query}&l={formatted_location}"

    # Prepare the Actor input
    run_input = {
        "scrapeJobs.searchUrl": search_url,
        "scrapeJobs.scrapeCompany": False,
        "count": count,
        "outputSchema": "raw",
        "findContacts": False,
        "findContacts.contactCompassToken": None,
        "findContacts.position": [
            "founder",
            "director",
        ],
    }

    # Run the Actor and wait for it to finish
    run = apify_client.actor("qA8rz8tR61HdkfTBL").call(run_input=run_input)
    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs

