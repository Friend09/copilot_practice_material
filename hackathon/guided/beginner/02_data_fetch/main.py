#!/usr/bin/env python3
"""
JSONPlaceholder analysis – who wrote the most posts?
"""

from typing import List, Dict
import requests
import collections


def fetch_posts() -> List[Dict]:
    """Return list of posts from JSONPlaceholder API."""
    # TODO: implement


def count_by_user(posts: List[Dict]) -> dict[int, int]:
    """Return a dict mapping userId to number of posts."""
    # TODO: implement


def main() -> None:
    posts = fetch_posts()
    counts = count_by_user(posts)
    user_id, total = max(counts.items(), key=lambda t: t[1])
    print(f"User {user_id} wrote {total} posts.")


if __name__ == "__main__":
    main()
