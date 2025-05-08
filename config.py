import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
USERS_FILE = os.path.join(os.path.dirname(__file__), "users.json")
LOG_FILE = os.path.join(os.path.dirname(__file__), "logs", "bot.log")