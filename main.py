import os
from telethon import TelegramClient

# Твои данные уже здесь
API_ID = 38098365 # Замени на свой реальный api_id (число), если еще не вписал
API_HASH = "631d10ea3bde2d7b4f3585a909502e2a"  # Твой api_hash
PHONE_NUMBER = "+49 15206544959"  # Твой номер телефона, к которому привязан телеграм

# Инициализируем клиент с привязкой к сессии
client = TelegramClient("my_telegram_session", API_ID, API_HASH)


async def download_circle_video(link: str):
  print("[*] Подключаемся к Telegram...")
  await client.start(phone=PHONE_NUMBER)

  # Парсим ссылку на сообщение (поддерживает публичные и приватные /c/ ссылки)
  if "/c/" in link:
    parts = link.split("/")
    chat_id = int("-100" + parts[-2])
    msg_id = int(parts[-1])
  else:
    parts = link.split("/")
    chat_id = parts[-2]
    msg_id = int(parts[-1])

  print(f"[*] Ищем кружочек в чате {chat_id} (сообщение #{msg_id})...")
  message = await client.get_messages(chat_id, ids=msg_id)

  # Проверяем, что в сообщении есть видеосообщение
  if message and message.video:
    print("[+] Кружочек найден! Скачиваем оригинальный видеофайл...")

    # Скачиваем прямо в текущую папку
    path = await message.download_media(file="./telegram_circle.mp4")
    print(f"[+] Готово! Видео сохранено: {os.path.abspath(path)}")
  else:
    print("[-] По этой ссылке нет видеосообщения (кружочка).")


with client:
  target_link = input(
      "Введи ссылку на сообщение-кружочек из Telegram: "
  ).strip()
  client.loop.run_until_complete(download_circle_video(target_link))