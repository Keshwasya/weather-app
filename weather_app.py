import requests
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()


api_key = os.getenv("API_KEY")
city = "Ottawa"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"