from storage.json_storage import get_user_links
from telegram import Update
from telegram.ext import ContextTypes

async def url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    links = await get_user_links(user_id)
    if not links:
        await update.message.reply_text("У вас немає доданих url.")
    else:
        msg = "\n".join([f"{l['url']} - {l['status']}" for l in links])
        await update.message.reply_text(msg)