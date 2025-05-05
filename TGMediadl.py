import os
import json
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel, InputMessagesFilterDocument, InputMessagesFilterPhotos, InputMessagesFilterVideo
from datetime import datetime
import pytz  # Timezone handling

# 🚀 Import credentials from config.json
with open('config.json', 'r') as file:
    config = json.load(file)

api_id = config['api_id']
api_hash = config['api_hash']
phone_number = config['phone_number']

save_folder = 'downloaded_media'

if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# 🧠 Media type filter mapping
filters = {
    "photos": InputMessagesFilterPhotos,
    "videos": InputMessagesFilterVideo,
    "files": InputMessagesFilterDocument
}

def find_channel(client, target_name):
    dialogs = client.get_dialogs()
    for dialog in dialogs:
        entity = dialog.entity
        if target_name.lower() in dialog.name.lower():
            print(f"✅ Found: {dialog.name} | ID: {entity.id} | Access Hash: {entity.access_hash}")
            return InputPeerChannel(channel_id=entity.id, access_hash=entity.access_hash)
    print("❌ Channel not found.")
    return None

with TelegramClient('media_session_filtered', api_id, api_hash) as client:
    client.start(phone=phone_number)

    channel_search_name = input("🔍 Enter partial channel name: ").strip()
    media_type = input("🎛️ Media type (photos/videos/files/all): ").strip().lower()
    date_from = input("📆 Enter start date (YYYY-MM-DD): ").strip()
    date_to = input("📆 Enter end date (YYYY-MM-DD): ").strip()

    # Convert dates to datetime format and set timezone
    tz = pytz.timezone('Asia/Dhaka')  # Set your timezone (here 'Asia/Dhaka' is used)
    from_date = tz.localize(datetime.strptime(date_from, "%Y-%m-%d"))
    to_date = tz.localize(datetime.strptime(date_to, "%Y-%m-%d"))

    channel = find_channel(client, channel_search_name)

    if channel:
        selected_filters = []
        if media_type in filters:
            selected_filters.append(filters[media_type])
        else:
            selected_filters = list(filters.values())

        for media_filter in selected_filters:
            media_folder = os.path.join(save_folder, media_filter.__name__.split('Filter')[-1].lower())  # Create folder for each media type
            if not os.path.exists(media_folder):
                os.makedirs(media_folder)

            print(f"⬇️ Downloading: {media_filter.__name__} to {media_folder}...")
            for message in client.iter_messages(channel, filter=media_filter):
                # Compare message date and filter date
                if message.date < from_date or message.date > to_date:
                    continue
                if message.media:
                    message.download_media(file=media_folder)

        print(f"✅ Download complete. Files saved in: {save_folder}")
    else:
        print("🚫 Channel not found.")
