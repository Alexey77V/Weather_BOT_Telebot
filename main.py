import telebot
from config import BOT_TOKEN, WEATHER_KEY
from weather_service import get_weather_data

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Напиши название города в России, чтобы узнать погоду.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    result = get_weather_data(message.text, WEATHER_KEY)
    
    if result["ok"]:
        text = (f"🌍 **Город:** {result['city']}\n"
                f"🌡 **Температура:** {result['temp']}°C\n"
                f"☁️ **Статус:** {result['desc']}\n"
                f"💧 **Влажность:** {result['hum']}%\n"
                f"💨 **Ветер:** {result['wind']} м/с")
    else:
        text = result["message"]
        
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()
