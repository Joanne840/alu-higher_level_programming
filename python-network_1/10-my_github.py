#!/usr/bin/python3
"""Fetch and display the authenticated GitHub user ID via Basic Auth."""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    response = requests.get("https://api.github.com/user", auth=(username, token))
    print(response.json().get("id"))
