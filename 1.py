import requests
import pandas as pd


def fetch_users_in_seattle(min_followers=200):
    url = 'https://api.github.com/search/users'
    params = {
        'q': 'location:Seattle followers:>200',
        'per_page': 100,
        'page': 1
    }

    users = []
    while True:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            break

        data = response.json()
        if 'items' not in data:
            break

        users.extend(data['items'])

        if len(data['items']) < 100:
            break

        params['page'] += 1

    return users


# Fetch users
users_data = fetch_users_in_seattle()

def clean_user_data(users):
    cleaned_users = []
    for user in users:
        cleaned_user = {
            'login': user.get('login', ''),
            'name': user.get('name', ''),
            'company': user.get('company', '').strip('@').upper().strip(),
            'location': user.get('location', ''),
            'email': user.get('email', ''),
            'hireable': user.get('hireable', ''),
            'bio': user.get('bio', ''),
            'public_repos': user.get('public_repos', ''),
            'followers': user.get('followers', ''),
            'following': user.get('following', ''),
            'created_at': user.get('created_at', '')
        }
        cleaned_users.append(cleaned_user)
    return pd.DataFrame(cleaned_users)

# Clean user data
users_df = clean_user_data(users_data)

# Save to CSV
users_df.to_csv('users.csv', index=False)
print('Data saved to users.csv')