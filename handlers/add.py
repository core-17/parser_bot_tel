import logging
from storage.json_storage import add_user_link
from telegram import Update
from telegram.ext import ContextTypes

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    username = update.effective_user.username or ""
    url = context.args[0] if context.args else None

    if not url:
        await update.message.reply_text("Ви не вказали посилання. Використайте /add <url>")
        return

    try:
        result = await add_user_link(user_id, username, url)
        logging.info(f"User {user_id} add url: {url} — {result}")
        await update.message.reply_text(result)
    except Exception as e:
        logging.error(f"Add error: {e}")
        await update.message.reply_text("Сталася помилка при додаванні.")