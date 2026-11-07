# Telegram-Video-Maker 🎬⚡

A fast, lightweight Python utility designed to extract, convert, and automate media retrieval directly from Telegram messages (including video messages / "kruzhok") using **Telethon**.

---

## 🚀 Features

* **Direct Telegram Extraction:** Automatically connects to Telegram via API to fetch media from public or private (`/c/`) channels and chats.
* **Video & Media Retrieval:** Download video messages ("kruzhok") directly into raw `.mp4` format without compression loss.
* **Smart Session Management:** Persistent session handling using `Telethon`—authorize once, and run seamlessly without repeated logins.
* **Developer Friendly:** Clean, asynchronous code structure built for fast terminal workflow integration.

---

## 🛠️ Prerequisites & Setup

### 1. Requirements

Ensure you have Python 3.8+ and `pip` installed:

```bash
python3 --version
pip --version
```

### 2. Dependencies

Install the required library using `pip`:

```bash
pip install telethon
```

*(Optional)* If you plan to extract specific frames/photos from videos:
```bash
pip install opencv-python
```

---

## 🔑 Getting Your Telegram Credentials

Before running the script, you need your personal `api_id` and `api_hash`: