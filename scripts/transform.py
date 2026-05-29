import pandas as pd
from scripts.logger import logger

def transform_weather_data(data, city="pune"):

    try:

        weather_data = {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather_condition": data["weather"][0]["main"]
        }

        df = pd.DataFrame([weather_data])

        logger.info("Weather data transformed successfully")

        return df

    except Exception as e:

        logger.error(f"Error transforming data: {e}")

        return None