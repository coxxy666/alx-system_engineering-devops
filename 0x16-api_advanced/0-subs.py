#!/usr/bin/python3
"""
Module for getting the number of subscribers for a given subreddit.
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If subreddit is invalid or there is an error, returns 0.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        response = get(url, headers=user_agent, allow_redirects=False)
        if response.status_code == 200:
            results = response.json()
            return results.get('data', {}).get('subscribers', 0)
    except Exception:
        return 0
    return 0

