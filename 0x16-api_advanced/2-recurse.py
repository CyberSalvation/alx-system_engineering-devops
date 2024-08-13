#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
	"""Recursively get all hot articles' titles for a given subreddit."""
	url = f"https://www.reddit.com/r/{subreddit}/hot.json"
	headers = {'User-Agent': 'Mozilla/5.0'}
	params = {'limit': 100}
	if after:
		params['after'] = after

		response = requests.get(url, headers=headers, params=params)

	if response.status_code != 200:
		return None

		data = response.json().get('data', {})
		children = data.get('children', [])
	if not children:
		return hot_list if hot_list else None

	for child in children:
		hot_list.append(child.get('data', {}).get('title'))

		after = data.get('after')
		if after:
			return recurse(subreddit, hot_list, after)
	else:
		return hot_list
