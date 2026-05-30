print("MAIN.PY STARTED")
from scripts.extract import extract_weather_data
from scripts.transform import transform_weather_data
from scripts.load import load_weather_data
from scripts.logger import logger
from scripts.init_db import *

def run_pipeline():
    print("PIPELINE RUNNING")

    logger.info("Pipeline started")

    raw_data = extract_weather_data()

    if raw_data:

        transformed_data = transform_weather_data(raw_data)

        if transformed_data is not None:

            load_weather_data(transformed_data)

    logger.info("Pipeline finished")

if __name__ == "__main__":

    run_pipeline()