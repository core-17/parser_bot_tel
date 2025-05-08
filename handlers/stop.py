import logging
from storage.json_storage import get_user_links, set_parse_status
from telegram import Update
from telegram.ext import ContextTypes

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    links = await get_user_links(user_id)
    if not links:
        await update.message.reply_text("У вас немає доданих url.")
        return

    url = context.args[0] if context.args else None
    if not url or url not in [l["url"] for l in links]:
        await update.message.reply_text("Вкажіть url для зупинки: /stop <url>")
        return

    try:
        await set_parse_status(user_id, url, "inactive")
        logging.info(f"User {user_id} stop parsing {url}")
        await update.message.reply_text(f"Парсинг для {url} зупинено.")
    except Exception as e:
        logging.error(f"Stop error: {e}")
        await update.message.reply_text("Сталася помилка при зупинці парсингу.")