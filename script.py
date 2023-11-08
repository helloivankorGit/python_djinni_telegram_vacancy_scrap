from telethon.sync import TelegramClient, events
import asyncio

# Replace these values with your own API credentials
api_id = ''
api_hash = ''

# Define your session name (can be any string)
session_name = 'djinni'

async def check_new_messages():
    async with TelegramClient(session_name, api_id, api_hash) as client:
        # Use the bot username or chat ID to target the specific bot/chat
        bot_entity = await client.get_input_entity('https://t.me/djinni_jobs_bot')

        @client.on(events.NewMessage(chats=bot_entity))
        async def handle_new_message(event):
            # Handle new messages here
            message_text = event.message.text
            print(f"New message: {message_text}")

        print("Listening for new messages...")
        await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(check_new_messages())
