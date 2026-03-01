import requests

def get_weather_data(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},RU&appid={api_key}&units=metric&lang=ru"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") == 200:
            return {
                "ok": True,
                "city": data["name"],
                "temp": round(data["main"]["temp"]),
                "desc": data["weather"][0]["description"],
                "hum": data["main"]["humidity"],
                "wind": data["wind"]["speed"]
            }
        return {"ok": False, "message": "❌ Город не найден."}
    except Exception:
        return {"ok": False, "message": "⚠️ Ошибка сервиса погоды."}
