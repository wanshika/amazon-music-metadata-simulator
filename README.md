# 🎶 Amazon Music Metadata Simulator

A backend system inspired by **Amazon Music's catalog architecture**, built to simulate how music metadata, rights, and ownership are ingested, validated, and served through scalable APIs.

---

## 🚀 Live Demo  
[![Live on Render](https://img.shields.io/badge/Live-Render-success?style=flat-square&logo=render)](https://amazon-music-metadata-api.onrender.com)

---

## 📌 Features

- 🎼 Simulates artists, tracks, and music rights using realistic data
- 🐘 Loads data into PostgreSQL using schema + ingestion scripts
- 🔎 Reconciles metadata to identify:
  - ❌ Expired rights
  - ⚠️ Tracks missing ownership
  - 🔁 Overlapping/conflicting rights periods
- 🌐 REST API built with Flask to access all insights
- ☁️ Deployable to Render with database integration

---

## 🧠 Tech Stack

| Layer | Tools |
|-------|-------|
| Backend | Python, Flask |
| Database | PostgreSQL |
| Hosting | Render |
| Data Simulation | Faker, Pandas |
| Reconciliation | pandas, datetime |
| API Format | REST (JSON)

---

## 📂 Project Structure

amazon-music-metadata-simulator/ ├── api/ # Flask app and route handlers ├── data/ # CSV generator and fake datasets ├── database/ # schema.sql and DB ingestion ├── reconciliation/ # Rights validation logic ├── tests/ # Unit test placeholder ├── requirements.txt # Project dependencies ├── render.yaml # Render deployment config └── README.md


---

## 🔗 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/health` | API health check |
| `/tracks/expired` | Tracks with expired rights |
| `/tracks/missing-rights` | Tracks without ownership |
| `/tracks/overlapping-rights` | Tracks with overlapping rights dates |

---

## ⚙️ Getting Started Locally

```bash
git clone https://github.com/YOUR_USERNAME/amazon-music-metadata-simulator.git
cd amazon-music-metadata-simulator
pip install -r requirements.txt

# Generate fake data
python data/generate_fake_data.py

# Load into PostgreSQL
python database/ingest_to_postgres.py

# Run Flask API
python api/app.py

Visit: http://127.0.0.1:5050/health

🧑‍💻 Author
Wanshika Patro
MS in Data Science | University at Buffalo

