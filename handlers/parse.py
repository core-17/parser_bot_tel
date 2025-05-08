import logging
from storage.json_storage import get_user_links, set_parse_status
from telegram import Update
from telegram.ext import ContextTypes

async def parse(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    links = await get_user_links(user_id)
    if not links:
        await update.message.reply_text("У вас немає доданих url для парсингу.")
        return

    url = context.args[0] if context.args else None
    freq = context.args[1] if len(context.args) > 1 else "5 хв"

    if not url or url not in [l["url"] for l in links]:
        await update.message.reply_text("Вкажіть url для парсингу: /parse <url> <частота>")
        return

    try:
        await set_parse_status(user_id, url, "active", freq)
        logging.info(f"User {user_id} start parsing {url} with freq {freq}")
        await update.message.reply_text(f"Парсинг для {url} запущено з частотою {freq}.")
    except Exception as e:
        logging.error(f"Parse error: {e}")
        await update.message.reply_text("Сталася помилка при запуску парсингу.")