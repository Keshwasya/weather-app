import requests
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()


api_key = os.getenv("API_KEY")
city = input("Enter city name: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"


response = requests.get(url)
data = response.json()

if data.get("cod") != 200:
    print("City not found or invalid API key.")
else:
    temperature = data["main"]["temp"]
    weather_description = data["weather"][0]["description"]
    city_name = data["name"]

    """Convert temp from Kelvin to Celsius"""
    temperature_celsius = temperature - 273.15

    print(f"City: {city_name}")
    print(f"Temperature: {temperature_celsius:.2f}°C")
    print(f"Weather: {weather_description}")
    print("")