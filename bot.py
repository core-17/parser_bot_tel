import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from config import TOKEN, LOG_FILE
from handlers import start, add, remove, url, help_command, parse, stop, settings

# Логування
logging.basicConfig(
    filename=LOG_FILE,
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.INFO,
)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("remove", remove))
    app.add_handler(CommandHandler("url", url))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("parse", parse))
    app.add_handler(CommandHandler("stop", stop))
    app.add_handler(CommandHandler("settings", settings))
    app.run_polling()

if __name__ == "__main__":
    main()