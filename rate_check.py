import requests
import os

# Retrieve the GitHub PAT from environment variables
github_pat = os.getenv('GITHUB_PAT')

headers = {
    'Authorization': f'Bearer {github_pat}'
}

response = requests.get('https://api.github.com/rate_limit', headers=headers)
print(response.text)

# Run in a loop to check the rate limit
while True:
    response = requests.get('https://api.github.com/rate_limit', headers=headers)
    print(response.text)