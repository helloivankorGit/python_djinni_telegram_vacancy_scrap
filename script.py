import asyncio
import logging
from telethon.sync import TelegramClient, events

# Configuration (consider moving to a config file or environment variables)
API_ID = ''
API_HASH = ''
SESSION_NAME = 'djinni'
BOT_URL = 'https://t.me/djinni_jobs_bot'

# Set up logging
logging.basicConfig(level=logging.INFO)

async def get_bot_entity(client):
    try:
        return await client.get_input_entity(BOT_URL)
    except Exception as e:
        logging.error(f"Error getting bot entity: {e}")
        return None

async def listen_for_messages(client, bot_entity):
    @client.on(events.NewMessage(chats=bot_entity))
    async def handle_new_message(event):
        message_text = event.message.text
        logging.info(f"New message: {message_text}")

async def main():
    async with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
        bot_entity = await get_bot_entity(client)
        if bot_entity:
            await listen_for_messages(client, bot_entity)
            logging.info("Listening for new messages...")
            await client.run_until_disconnected()
        else:
            logging.error("Bot entity not found. Exiting...")

if __name__ == '__main__':
    asyncio.run(main())
