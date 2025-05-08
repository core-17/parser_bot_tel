from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

MAIN_KEYBOARD = [["/add", "/remove"], ["/url", "/help"], ["/parse", "/stop"], ["/settings"]]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = ReplyKeyboardMarkup(MAIN_KEYBOARD, resize_keyboard=True)
    await update.message.reply_text("Оберіть дію:", reply_markup=reply_markup)