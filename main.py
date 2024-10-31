import os
import requests

# Get the GitHub token from environment variables
GITHUB_TOKEN_TDS = "dummy"

if not GITHUB_TOKEN_TDS:
    raise ValueError("GitHub token not found. Set GITHUB_TOKEN environment variable.")

headers = {
    "Authorization": f"token {GITHUB_TOKEN_TDS}",
    "Accept": "application/vnd.github.v3+json"
}

# Example API request to get users in Seattle with over 200 followers
url = "https://api.github.com/search/users?q=location:Seattle+followers:>200"
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)  # Process your data here
else:
    print(f"Failed to fetch data: {response.status_code}")
