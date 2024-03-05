#!/usr/bin/python3
"""
0-subs
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the
    number of subscribers for a given subreddit.
    If the subreddit is invalid or not found, returns 0.

    Args:
        subreddit: The name of the subreddit to query.

    Returns:
        The number of subscribers of the subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'MyBot/1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
