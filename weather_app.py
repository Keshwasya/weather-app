import requests
import os
import datetime
from dotenv import load_dotenv

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
    sunrise_unix = data["sys"]["sunrise"]
    sunset_unix = data["sys"]["sunset"]
    city_name = data["name"]
    temperature = data["main"]["temp"]
    temperature_celsius = temperature - 273.15 # Kelvin to Celsius
    temperature_fahrenheit = (temperature - 273.15) * 9/5 + 32 # Kelvin to Fahrenheit
    weather_description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    
    # Convert sunrise/sunset to readable format
    sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime('%H:%M:%S')
    sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"]).strftime('%H:%M:%S')

    # Convert m/s to km/h
    wind_speed_kmh = wind_speed * 3.6  

    # Print the weather information
    print(f"City: {city_name}")
    print(f"Temperature: {temperature:.2f}°C")
    print(f"Weather: {weather_description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed_kmh:.2f} km/h")
    print(f"Sunrise: {sunrise}")
    print(f"Sunset: {sunset}")