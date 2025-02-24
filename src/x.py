import requests
import time
from bs4 import BeautifulSoup
import re

class X:
    def __init__(self, username="infecteddotfun"):
        self.url = f"https://nitter.net/{username}"
        self.headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"
        }

    def scrape_tweets(self, username, count=5):
        url = f"https://nitter.net/{username}"
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        try:
            time.sleep(2)
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                print(f"Error: HTTP status {response.status_code}")
                return []
            soup = BeautifulSoup(response.text, "html.parser")
            tweets = [tweet.text.strip() for tweet in soup.find_all("div", class_="tweet-content")]
            if not tweets:
                print("Nothing found on X, check account or scrapper.")
            return tweets[:count]
        
        except requests.exceptions.RequestException as e:
            print("Error in request :", e)
            return []

    def extract_eth_addresses(self, tweets):
        eth_pattern = r"\b0x[a-fA-F0-9]{40}\b"
        addresses = []
        for tweet in tweets:
            found_addresses = re.findall(eth_pattern, tweet)
            if found_addresses:
                addresses.extend(found_addresses)

        return addresses
