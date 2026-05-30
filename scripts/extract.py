import requests
import os
from dotenv import load_dotenv
from scripts.logger import logger

load_dotenv()

API_KEY = os.getenv("API_KEY")

def extract_weather_data(city="pune"):
    

    try:
        print("API_KEY exists:", API_KEY is not None)

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        print("Making API request...")

        response = requests.get(url, timeout=10)

        print("Status Code:", response.status_code)

        print("Response Preview:", response.text[:200])

        response.raise_for_status()

        data = response.json()

        print("DATA RECEIVED")

        logger.info("Weather data extracted successfully")

        return data

    except requests.exceptions.RequestException as e:

        print("REQUEST ERROR:", e)

        logger.error(f"Error extracting weather data: {e}")

        return None