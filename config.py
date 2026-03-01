import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN", "ТВОЙ_ТОКЕН")
WEATHER_KEY = os.getenv("WEATHER_KEY", "ТВОЙ_API_КЛЮЧ")
