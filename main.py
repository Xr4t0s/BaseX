from src.x import X
from src.telegram_bot import TelegramBot
import time
import os
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv("TG_ID")
api_hash = os.getenv("TG_HASH")
phone_number = os.getenv("PHONE")
contact_username = os.getenv("BROKER")
target = os.getenv("TARGET")

x_scraper = X()
telegram_bot = TelegramBot(api_id, api_hash, phone_number, contact_username)

def main():
    while True:
        print("🔄 Checking new posts...")
        tweets = x_scraper.scrape_tweets(target)
        addresses = x_scraper.extract_eth_addresses(tweets)

        if addresses:
            for address in addresses:
                message = f"`{address}`"
                print(f"📨 Sending with telegram : {message}")
                telegram_bot.send(message)

        else:
            print("🔍 No new contract... Retrying in 1 minute.")

        time.sleep(60)

if __name__ == "__main__":
    main()
