# Weather ETL Pipeline 🌦️

Automated ETL pipeline built using Python and PostgreSQL to fetch, transform, and store real-time weather data from OpenWeather API.

## 🚀 Features

- Extract real-time weather data using API
- Transform and clean JSON data using Pandas
- Load processed data into PostgreSQL
- Logging and error handling
- Environment variable configuration
- Automated workflow support

---

## 🛠️ Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- OpenWeather API
- Git & GitHub

---

## 📂 Project Structure

```bash
weather-etl-pipeline/
│
├── data/
├── logs/
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── logger.py
│
├── .env
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ ETL Workflow

```text
Extract → Transform → Load
```

1. Extract weather data from API
2. Transform JSON into structured format
3. Load cleaned data into PostgreSQL

---

## ▶️ Run Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run pipeline:

```bash
python main.py
```

---

## 📊 Sample SQL Query

```sql
SELECT city, AVG(temperature)
FROM weather_data
GROUP BY city;
```

