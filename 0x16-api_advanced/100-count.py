#!/usr/bin/python3
"""
100-count
"""

import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit: The name of the subreddit to query.
        word_list: A list of keywords to count occurrences of.
        hot_list: A list to store the titles of hot articles.
        after: A parameter used for pagination.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {'User-Agent': 'MyBot/1.0'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if not posts:
            count_dict = {}
            for title in hot_list:
                for word in title.lower().split():
                    word = word.rstrip('.!_')  # Remove trailing punctuation
                    if word in word_list:
                        count_dict[word] = count_dict.get(word, 0) + 1
            sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print("{}: {}".format(word, count))
            return
        for post in posts:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        count_words(subreddit, word_list, hot_list, after)
    else:
        print(None)
