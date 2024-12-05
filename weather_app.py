import requests
import os
from dotenv import load_dotenv
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QLineEdit, QPushButton, QWidget

# Load environment variables from the .env file
load_dotenv()

# Get the API key from the .env file
api_key = os.getenv("API_KEY")

class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 400, 200)

        # Create layout and widgets
        layout = QVBoxLayout()

        self.city_label = QLabel("Enter City Name:")
        layout.addWidget(self.city_label)

        self.city_input = QLineEdit()
        layout.addWidget(self.city_input)

        self.search_button = QPushButton("Get Weather")
        layout.addWidget(self.search_button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        # Set layout for the central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Connect button to the function
        self.search_button.clicked.connect(self.get_weather)

    def get_weather(self):
        city = self.city_input.text()
        if city:
            weather_info = self.fetch_weather(city)
            self.result_label.setText(weather_info)
        else:
            self.result_label.setText("Please enter a city name.")

    def fetch_weather(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            response = requests.get(url)
            data = response.json()
            if data.get("cod") != 200:
                return "City not found!"

            # Extract weather details
            temperature = data["main"]["temp"] - 273.15  # Convert Kelvin to Celsius
            weather_description = data["weather"][0]["description"]
            return f"Temperature: {temperature:.2f}°C\nWeather: {weather_description}"
        except Exception as e:
            return "Failed to fetch weather data."

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
