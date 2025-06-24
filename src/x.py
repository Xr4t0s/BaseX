import requests
import time
from bs4 import BeautifulSoup
import re

class X:
    def __init__(self, username="infecteddotfun"):
        self.username = username
        self.base_url = f"https://nitter.net/{username}"
        self.headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"
        }

    def scrape_section(self, section="", count=5):
        try:
            count = int(count)
            url = f"{self.base_url}{section}"
            time.sleep(2)
            response = requests.get(url, headers=self.headers)
            if response.status_code != 200:
                print(f"Erreur HTTP {response.status_code} sur {url}")
                return []

            soup = BeautifulSoup(response.text, "html.parser")
            tweets = [tweet.text.strip() for tweet in soup.find_all("div", class_="tweet-content")]
            if not tweets:
                print(f"Aucun contenu trouvé dans {url}")
            return tweets[:count]

        except Exception as e:
            print(f"Erreur pendant le scraping de {section or 'tweets'} :", e)
            return []

    def scrape_all(self, count=5):
        count = int(count)
        tweets = self.scrape_section("", count)
        replies = self.scrape_section("/with_replies", count)
        return tweets + replies

    def extract_eth_addresses(self, tweets):
        eth_pattern = r"\b0x[a-fA-F0-9]{40}\b"
        addresses = []
        for tweet in tweets:
            found = re.findall(eth_pattern, tweet)
            addresses.extend(found)
        return addresses
