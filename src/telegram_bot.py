from telethon import TelegramClient

class TelegramBot:
    def __init__(self, api_id, api_hash, phone_number, contact_username):
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone_number = phone_number
        self.contact_username = contact_username
        self.client = TelegramClient("session_name", api_id, api_hash)

    async def send_message(self, message):
        await self.client.start(self.phone_number)
        await self.client.send_message(self.contact_username, message)

    def send(self, message):
        with self.client:
            self.client.loop.run_until_complete(self.send_message(message))
