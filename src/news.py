import requests
import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def get_headlines(topics=["technology", "sports"]):
    headlines = []

    for topic in topics:
        url = (
            f"https://newsapi.org/v2/top-headlines"
            f"?category={topic}&pageSize=3&language=en&apiKey={NEWS_API_KEY}"
        )
        response = requests.get(url)
        data = response.json()

        if data.get("status") == "ok":
            for article in data.get("articles", []):
                headlines.append({
                    "topic": topic,
                    "title": article["title"],
                    "description": article.get("description", "")
                })

    return headlines


if __name__ == "__main__":
    headlines = get_headlines()
    for h in headlines:
        print(f"[{h['topic'].upper()}] {h['title']}")
