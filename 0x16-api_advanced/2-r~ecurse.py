#!/usr/bin/python3
"""
A function that queries Reddit API and returns a list containing the titles of
all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively fetches and appends titles of hot articles for a given subreddi
    using the Reddit API. Returns a list of titles. If the subreddit is invalid
    returns None.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Google Chrome Version 119.0.6045.106'}

    if after:
        url = '{}&after={}'.format(url, after)

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            return hot_list

        for post in posts:
            hot_list.append(post['data']['title'])

        after = data.get('data', {}).get('after')
        if after:
            return recurse(subreddit, hot_list, after)

    return hot_list
