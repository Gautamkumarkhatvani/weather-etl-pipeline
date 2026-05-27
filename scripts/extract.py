import requests
import os
from dotenv import load_dotenv
from scripts.logger import logger

load_dotenv()

API_KEY = os.getenv("API_KEY")

def extract_weather_data(city="Pune"):

    try:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        response.raise_for_status()

        data = response.json()

        logger.info("Weather data extracted successfully")

        return data

    except requests.exceptions.RequestException as e:

        logger.error(f"Error extracting weather data: {e}")

        return None