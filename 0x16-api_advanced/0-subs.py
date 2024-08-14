#!/usr/bin/python3
"""Module for querying the number of subscribers in a subreddit."""
import requests
def number_of_subscribers(subreddit):
	"""Return the number of subscribers for a given subreddit."""
	url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
	headers = {'User-Agent': 'Mozilla/5.0 (compatible; my-reddit-app/0.1)'}
	
	response = requests.get(url, headers=headers)

	if response.status_code == 200:
		data = response.json().get('data', {})
		return data.get('subscribers', 0)
	return 0
