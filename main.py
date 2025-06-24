from src.x import X
from src.telegram_bot import TelegramBot
import time
import sys
import os
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv("TG_ID")
api_hash = os.getenv("TG_HASH")
phone_number = os.getenv("PHONE")
contact_username = os.getenv("CONTACT")
target = os.getenv("TARGET")

x_scraper = X(target)
telegram_bot = TelegramBot(api_id, api_hash, phone_number, contact_username)

def main():
    print("If first login we need to connect")
    telegram_bot.send("This is the first login message, if you see this it means that all is working good")
    while True:
        print("🔄 Checking new posts...")
        tweets = x_scraper.scrape_all(count=10)
        addresses = x_scraper.extract_eth_addresses(tweets)

        if addresses:
            for address in addresses:
                message = f"`{address}`"
                print(f"📨 Sending with telegram : {message}")
                telegram_bot.send(message)
                break
            break

        else:
            print("🔍 No new contract... Retrying in 10 seconds.")

        time.sleep(10)

if __name__ == "__main__":
    main()
