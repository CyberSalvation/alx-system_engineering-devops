#!/usr/bin/python3
import requests
import re
from collections import defaultdict

def count_words(subreddit, word_list):
	"""Print a sorted count of given keywords in the titles of hot articles for a given subreddit."""
	def fetch_hot_posts(subreddit, after=None):
        """Recursive function to fetch hot posts."""
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
        after = data.get('after')

        titles = [child.get('data', {}).get('title', '') for child in children]
        if after:
            return titles + fetch_hot_posts(subreddit, after)
        return titles

    def count_keywords(titles, word_list):
        """Count occurrences of keywords in titles."""
        word_count = defaultdict(int)
        for title in titles:
            title = title.lower()
            for word in word_list:
                # Count whole words only, case-insensitive
                word_count[word] += len(re.findall(rf'\b{re.escape(word)}\b', title))
        return word_count

    titles = fetch_hot_posts(subreddit)
    if titles is None:
        return

    word_list = [word.lower() for word in word_list]
    word_count = count_keywords(titles, word_list)

    # Sort by count descending, then alphabetically ascending
    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_word_count:
        if count > 0:
            print(f"{word}: {count}")
