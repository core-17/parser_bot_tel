import logging
from storage.json_storage import get_user_links, set_parse_status
from telegram import Update
from telegram.ext import ContextTypes

async def settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    links = await get_user_links(user_id)
    if not links:
        await update.message.reply_text("У вас немає доданих url.")
        return

    url = context.args[0] if context.args else None
    freq = context.args[1] if len(context.args) > 1 else None
    if not url or url not in [l["url"] for l in links] or not freq:
        await update.message.reply_text("Вкажіть url і нову частоту: /settings <url> <частота>")
        return

    try:
        await set_parse_status(user_id, url, "active", freq)
        logging.info(f"User {user_id} change settings {url} freq {freq}")
        await update.message.reply_text(f"Частоту парсингу для {url} змінено на {freq}.")
    except Exception as e:
        logging.error(f"Settings error: {e}")
        await update.message.reply_text("Сталася помилка при зміні налаштувань.")