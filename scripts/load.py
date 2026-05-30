from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from scripts.logger import logger

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

print("DB_USER =", DB_USER)
print("DB_HOST =", DB_HOST)
print("DB_PORT =", DB_PORT)

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

def load_weather_data(df):

    try:
        df.to_sql(
            "weather_data",
            engine,
            if_exists="append",
            index=False
        )
        print("Data inserted successfully!")

        logger.info("Data loaded into PostgreSQL successfully")

    except Exception as e:
        print("DATABASE ERROR:", e)
        logger.error(f"Error loading data: {e}")