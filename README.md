# Telegram Media Downloader

A Python script to download media (photos, videos, or documents) from a Telegram channel using the Telethon library. Supports date-range filtering and media-type separation into folders.

---

## 🔧 Features

- Download **photos**, **videos**, or **files** from any public/private Telegram channel you have access to.
- Filter by **date range**.
- Media saved in separate folders based on type.
- Uses **timezone-aware** date filtering.

---

## 🚀 Quick Start

### 1. Clone the Repository

    git clone https://github.com/your-username/telegram-media-downloader.git
    cd telegram-media-downloader
2. Install Requirements
    pip install -r requirements.txt
📱 Get Telegram API Credentials
Go to https://my.telegram.org
Log in with your Telegram number.
Click on API Development Tools.
Fill in the form to create a new app.
Copy your api_id and api_hash.

🔐 Configuration
Create a file named config.json in the root directory with the following content:

json
Copy
Edit
{
  "api_id": 123456,
  "api_hash": "your_api_hash_here",
  "phone_number": "+1234567890"
}


🛠️ **Usage**
Run the script:

python TGMediadl.py

Follow the on-screen prompts:

Enter partial channel name (e.g., news or updates)

Choose media type: photos, videos, files, or all

Enter start date and end date (format: YYYY-MM-DD)

**Media will be downloaded into:**

downloaded_media/photos/
downloaded_media/videos/
downloaded_media/files/

📂 **File Structure**

telegram-media-downloader/
├── Bot.py
├── config.json           # Your Telegram API credentials (do not upload)
├── requirements.txt
├── README.md
├── .gitignore
└── downloaded_media/     # Auto-created for saving media
