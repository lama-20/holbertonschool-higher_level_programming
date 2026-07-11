#!/usr/bin/python3
"""Module to fetch and process posts data from JSONPlaceholder API."""
import csv
import requests


def fetch_and_print_posts():
    """Fetch all posts from JSONPlaceholder and print status code
    and titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch all posts from JSONPlaceholder and save them into
    a CSV file called posts.csv."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        data = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"],
            }
            for post in posts
        ]

        fieldnames = ["id", "title", "body"]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
