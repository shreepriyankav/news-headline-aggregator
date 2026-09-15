import os

import requests
from dotenv import load_dotenv


load_dotenv()


def fetch_headlines():
    api_key = os.getenv("NEWS_API_KEY")

    url = "https://gnews.io/api/v4/top-headlines"

    params = {
        "apikey": api_key,
        "lang": "en",
        "country": "in",
        "max": 10
    }

    response = requests.get(url, params=params, timeout=10)

    response.raise_for_status()

    data = response.json()

    return data["articles"]


if __name__ == "__main__":
    articles = fetch_headlines()

    print(f"✅ Successfully fetched {len(articles)} headlines\n")

    for article in articles:
        print("Title:", article.get("title"))
        print("Source:", article.get("source", {}).get("name"))
        print("Published:", article.get("publishedAt"))
        print("URL:", article.get("url"))
        print("-" * 80)
