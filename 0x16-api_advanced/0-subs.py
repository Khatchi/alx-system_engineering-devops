#!/usr/bin/python3
"""a func that queries Reddit API: returns the num
of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit using the
    Reddit API. If the subreddit is invalid or not provided, returns 0.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-agent': 'Google Chrome Version 119.0.6045.106'}

    response = requests.get(url, headers=headers).json()

    return response.get('data', {}).get('subscribers', 0)
