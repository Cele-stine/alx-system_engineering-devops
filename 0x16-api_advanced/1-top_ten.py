#!/usr/bin/python3
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        print(f"Top 10 hot posts in r/{subreddit}:\n")
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print("None")

# Example usage:
subreddit = "python"
top_ten(subreddit)

