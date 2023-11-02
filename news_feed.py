'''
This file contains the NewsFeed class which retrieves and provides the latest tech news.
'''
import requests
class NewsFeed:
    def __init__(self):
        self.url = "https://api.example.com/news"  # Replace with the actual news API URL
    def get_news(self):
        # Retrieve the latest news from the API
        response = requests.get(self.url)
        if response.status_code == 200:
            news = response.json()
            return news
        else:
            return "Failed to retrieve news"