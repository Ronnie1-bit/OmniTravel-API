# 🌍 OmniTravel API: Real-Time Intelligence Engine
A high-performance FastAPI backend that orchestrates global weather data and currency exchange rates into a persistent SQLite audit log.

## 🚀 Overview
OmniTravel acts as a central hub for travelers, providing instant local insights by connecting to multiple third-party REST APIs. It doesn't just fetch data; it archives every search for historical analysis.

## 🛠️ Tech Stack
- [cite_start]**Framework:** FastAPI (Asynchronous Python) 
- [cite_start]**Database:** SQLite3 (Persistent Storage) 
- [cite_start]**APIs:** Open-Meteo (Geocoding/Weather), ExchangeRate-API (Currency) 

## 📋 Installation & Setup
Follow these steps to run the project locally:

1. **Clone the Project:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/OmniTravel-API.git](https://github.com/YOUR_USERNAME/OmniTravel-API.git)
   cd OmniTravel-API

2. **Install the Libraries**
   ```bash
   pip install fastapi requests uvicorn

4. **Use the command line in cmd of the file in the directory you saved**
    ```bash
    fastapi dev omni.py
