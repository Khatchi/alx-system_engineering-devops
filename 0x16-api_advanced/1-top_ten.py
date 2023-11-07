#!/usr/bin/python3
"""
A function that queries Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit using the
    Reddit API. If the subreddit is invalid or not provided, it prints None.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Google Chrome Version 119.0.6045.106'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                title = post['data']['title']
                print(title)
    else:
        print(None)
