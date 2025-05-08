import logging
from storage.json_storage import remove_user_link
from telegram import Update
from telegram.ext import ContextTypes

async def remove(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    url = context.args[0] if context.args else None

    if not url:
        await update.message.reply_text("Ви не вказали посилання. Використайте /remove <url>")
        return

    try:
        result = await remove_user_link(user_id, url)
        logging.info(f"User {user_id} remove url: {url} — {result}")
        await update.message.reply_text(result)
    except Exception as e:
        logging.error(f"Remove error: {e}")
        await update.message.reply_text("Сталася помилка при видаленні.")