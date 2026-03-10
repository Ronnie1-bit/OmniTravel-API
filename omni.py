from fastapi import FastAPI, HTTPException
import sqlite3
import requests
app = FastAPI()
@app.on_event("startup")
def create():
	connections = sqlite3.connect("My_Database1.db")
	cursor = connections.cursor()
	cursor.execute("CREATE TABLE IF NOT EXISTS travel( Slno INTEGER  PRIMARY KEY AUTOINCREMENT, City_name TEXT, Weather REAL, Price REAL, Date_Time DATETIME DEFAULT CURRENT_TIMESTAMP)")
	connections.commit()
	connections.close()
@app.get("/{city_name}/price/INR")
def read( city_name: str):
	url1 = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1"
	response1 = requests.get(url1, timeout=5).json()
	if "results" not in response1 or not response1["results"]:
		raise HTTPException(status_code = 404, detail = "Not Found")
	results = response1["results"][0]
	lat,lon = results["latitude"], results["longitude"]
	url2 = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
	response2 = requests.get(url2, timeout=5).json()
	if "current_weather" not in response2: 
		raise HTTPException(status_code= 501, detail = "current weather not found")
	Temperature = response2["current_weather"]["temperature"]
	url3 = "https://open.er-api.com/v6/latest/USD"
	response3 = requests.get(url3, timeout=5).json()
	if "rates" not in response3 or "INR" not in response3["rates"]:
		raise HTTPException(status_code= 503, detail ="Price not found")
	Price = response3["rates"]["INR"]
	connections = sqlite3.connect("My_Database1.db")
	cursor = connections.cursor()
	cursor.execute("INSERT INTO travel (City_name, Weather, Price) VALUES(?, ?, ?)", (city_name, Temperature, Price))
	connections.commit()
	connections.close()
	return{ "message" : "Created Successfully", "Price" : Price, "Temperature" : Temperature, "Place" : city_name  }
@app.get("/history")
def get_history():
    connections = sqlite3.connect("My_Database1.db")
    connections.row_factory = sqlite3.Row 
    cursor = connections.cursor()
    cursor.execute("SELECT * FROM travel ORDER BY Date_Time DESC")
    rows = cursor.fetchall()
    connections.close()
    return {"search_count": len(rows), "history": [dict(row) for row in rows]}