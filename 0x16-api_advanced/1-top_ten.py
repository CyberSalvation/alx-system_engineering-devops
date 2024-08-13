#!/usr/bin/python3
import requests

def top_ten(subreddit):
	"""Print the titles of the first 10 hot posts listed for a given subreddit."""
	url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
	headers = {'User-Agent': 'Mozilla/5.0'}

	response = requests.get(url, headers=headers)

	if response.status_code == 200:
		posts = response.json().get('data', {}).get('children', [])
		for post in posts:
			print(post.get('data', {}).get('title'))
	else:
		print(None)
