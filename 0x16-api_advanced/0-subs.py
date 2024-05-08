#!/usr/bin/python3
"""
Importing requests module
"""

# from requests import get


# def number_of_subscribers(subreddit):
#     """
#     function that queries the Reddit API and returns the number of subscribers
#     (not active users, total subscribers) for a given subreddit.
#     """

#     if subreddit is None or not isinstance(subreddit, str):
#         return 0

#     user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
#     url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
#     response = get(url, headers=user_agent)
#     all_data = response.json()

#     try:
#         return all_data.get('data').get('subscribers')

#     except:
#         return 0


import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-Agent': 'My Reddit Script by /u/yourusername'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    try:
        response = requests.get(url, headers=user_agent)
        response.raise_for_status()  # Raise an exception for HTTP errors
        all_data = response.json()
        return all_data['data']['subscribers']
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0
    except KeyError:
        # Handle cases where the JSON structure doesn't match expectations
        return 0