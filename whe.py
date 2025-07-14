import requests

# OpenWeatherMap API details
API_KEY = "151f4ca33806415989f9ffebbe02c701"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetches and displays weather details for a given city."""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Parse JSON response
        data = response.json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        print("\n🌍 Weather Report 🌍")
        print(f"📍 City: {city.capitalize()}")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"☁️ Condition: {weather.capitalize()}\n")

    except requests.exceptions.RequestException as e:
        print("⚠️ Error: Unable to fetch weather data. Please check your internet connection.")
    except KeyError:
        print("⚠️ Error: Invalid city name. Please enter a valid city.")

if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    if city:
        get_weather(city)
    else:
        print("⚠️ Error: City name cannot be empty.")