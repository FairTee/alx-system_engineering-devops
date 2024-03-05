#!/usr/bin/python3
"""
2-recurse
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.

    Args:
        subreddit: The name of the subreddit to query.
        hot_list: A list to store the titles of hot articles.
        after: A parameter used for pagination.

    Returns:
        A list containing the titles of all hot articles for the given subreddit,
        or None if no results are found.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {'User-Agent': 'MyBot/1.0'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if not posts:
            return hot_list if hot_list else None
        for post in posts:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
