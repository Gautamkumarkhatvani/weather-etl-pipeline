# 🌦️ Weather ETL Pipeline

An end-to-end Data Engineering project that extracts real-time weather data from the OpenWeather API, transforms it into a structured format, and loads it into PostgreSQL for analytics and visualization.

---

## 🚀 Project Overview

This project demonstrates a complete ETL (Extract, Transform, Load) workflow using Python, PostgreSQL, Docker, and Power BI.

The pipeline automatically:

* Extracts real-time weather data from OpenWeather API
* Transforms and cleans JSON responses
* Loads processed data into PostgreSQL
* Stores historical weather records
* Supports SQL-based analytics
* Visualizes data through Power BI dashboards
* Runs inside Docker containers using Docker Compose

---

## 🏗️ Architecture

```text
OpenWeather API
       │
       ▼
   Extract
       │
       ▼
  Transform
       │
       ▼
 PostgreSQL
       │
       ▼
 SQL Analytics
       │
       ▼
 Power BI Dashboard
```

---

## 🛠️ Tech Stack

### Programming & Data Processing

* Python
* Pandas

### Database

* PostgreSQL
* SQLAlchemy

### APIs

* OpenWeather API

### Containerization

* Docker
* Docker Compose

### Visualization

* Power BI

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```bash
weather-etl-pipeline/
│
├── data/
│
├── dashboard/
│   └── weather_dashboard.png
│
├── logs/
│   └── pipeline.log
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── init_db.py
│   └── logger.py
│
├── sql/
│   └── analytics_queries.sql
│
├── .dockerignore
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── main.py
├── README.md
└── requirements.txt
```

---

## ⚙️ ETL Workflow

### 1. Extract

Fetches real-time weather data from OpenWeather API.

Example fields:

* Temperature
* Humidity
* Weather Condition
* City

### 2. Transform

Converts raw JSON into a structured tabular format using Pandas.

### 3. Load

Stores cleaned data into PostgreSQL for analysis and reporting.

---

## 🐳 Docker Setup

Build and start all services:

```bash
docker compose up --build
```

Run in detached mode:

```bash
docker compose up -d
```

Stop services:

```bash
docker compose down
```

---

## 🗄️ Database Schema

```sql
CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    temperature FLOAT,
    humidity INT,
    weather_condition VARCHAR(50),
    recorded_at TIMESTAMP
);
```

---

## 📊 SQL Analytics Examples

### Average Temperature by City

```sql
SELECT city,
       AVG(temperature) AS avg_temperature
FROM weather_data
GROUP BY city;
```

### Average Humidity by City

```sql
SELECT city,
       AVG(humidity) AS avg_humidity
FROM weather_data
GROUP BY city;
```

### Most Common Weather Condition

```sql
SELECT weather_condition,
       COUNT(*) AS frequency
FROM weather_data
GROUP BY weather_condition
ORDER BY frequency DESC;
```

---

## 📈 Power BI Dashboard

The dashboard includes:

* Total Records
* Average Temperature
* Average Humidity
* Temperature by City
* Weather Distribution
* Historical Weather Trends

Add dashboard screenshot:

```text
dashboard/weather_dashboard.png
```

---

## 🔒 Environment Variables

Create a `.env` file:

```env
API_KEY=your_api_key

DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=postgres
DB_PORT=5432
DB_NAME=weather_pipeline
```

---

## ▶️ Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run ETL pipeline:

```bash
python main.py
```

---

## 🎯 Key Skills Demonstrated

* ETL Pipeline Development
* REST API Integration
* Data Transformation with Pandas
* PostgreSQL Database Management
* SQL Analytics
* Docker Containerization
* Docker Compose Orchestration
* Power BI Dashboarding
* Logging & Error Handling
* Environment Variable Management

---

## 🚀 Future Improvements

* Apache Airflow Integration
* AWS Deployment
* Historical Weather Forecast Storage
* Real-Time Streaming with Kafka
* Automated Scheduling

---

## 👨‍💻 Author

GK

Aspiring Data Engineer focused on building scalable data pipelines, automation workflows, and analytics solutions using Python, SQL, Docker, and modern data engineering tools.
