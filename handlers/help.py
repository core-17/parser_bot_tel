from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/add <url> — додати url\n"
        "/remove <url> — видалити url\n"
        "/url — список ваших url\n"
        "/parse — запустити парсинг\n"
        "/stop — зупинити парсинг\n"
        "/settings — налаштування\n"
        "/help — допомога"
    )