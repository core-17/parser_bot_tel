import json
import asyncio
import os
from config import USERS_FILE

_LOCK = asyncio.Lock()

async def add_user_link(user_id, username, url):
    async with _LOCK:
        data = await _read()
        if user_id not in data:
            data[user_id] = {"username": username, "links": []}
        for link in data[user_id]["links"]:
            if link["url"] == url:
                return "Цей url вже додано."
        data[user_id]["links"].append({"url": url, "status": "inactive", "freq": "5 хв"})
        await _write(data)
        return "Url додано!"

async def remove_user_link(user_id, url):
    async with _LOCK:
        data = await _read()
        if user_id not in data:
            return "Користувача не знайдено."
        links = data[user_id]["links"]
        new_links = [l for l in links if l["url"] != url]
        if len(links) == len(new_links):
            return "Url не знайдено."
        data[user_id]["links"] = new_links
        await _write(data)
        return "Url видалено!"

async def get_user_links(user_id):
    async with _LOCK:
        data = await _read()
        if user_id not in data:
            return []
        return data[user_id]["links"]

async def set_parse_status(user_id, url, status, freq=None):
    async with _LOCK:
        data = await _read()
        if user_id not in data:
            return
        for link in data[user_id]["links"]:
            if link["url"] == url:
                link["status"] = status
                if freq:
                    link["freq"] = freq
        await _write(data)

async def _read():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

async def _write(data):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)