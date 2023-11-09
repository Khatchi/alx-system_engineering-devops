#!/usr/bin/python3
"""This module counts words using reddit API """

import re
import requests



def count_words(subreddit, word_list, counts={}, after=None):
    """
    Queries the Reddit API, parses the titles of hot articles,
    and prints a sorted count of given keywords.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Google Chrome Version 119.0.6045.106'}

    response = requests.get(url, params={"after": after}, headers=headers)

    if response.status_code == 200:
        after = response.json().get("data").get("after")
        if not after:
            counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, occurence in counts:
                print('{}: {}'.format(word, occurence))
            return
        for post in response.json().get("data").get("children"):
            for word in word_list:
                pattern = re.escape(word.lower())
                target = post.get('data').get('title').lower()
                occ = len(re.findall(r'\b{}\b'.format(pattern), target))
                if occ > 0:
                    counts[word.lower()] = counts.get(word, 0) + occ
        return count_words(subreddit, word_list, counts, after)
