from flask import Flask, request, jsonify, render_template
import requests
import sqlite3
import time
import threading
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

API_KEY = '82d3ca2cffa6484002ebf8471a1de406'  # Replace with your OpenWeatherMap API key
CITY_IDS = {
    'Delhi': 1273294,
    'Mumbai': 1275339,
    'Chennai': 1264527,
    'Bangalore': 1277333,
    'Kolkata': 1275004,
    'Hyderabad': 1269843
}
UPDATE_INTERVAL = 120  # Fetch data every 2 minutes

def init_db():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            main TEXT,
            temp REAL,
            feels_like REAL,
            dt INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def fetch_weather_data():
    while True:
        for city, city_id in CITY_IDS.items():
            url = f'http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={API_KEY}'
            response = requests.get(url)
            data = response.json()
            print(f"Response for {city}: {data}")  # Log the response
            save_weather_data(city, data)
        time.sleep(UPDATE_INTERVAL)


def save_weather_data(city, data):
    try:
        conn = sqlite3.connect('weather.db')
        c = conn.cursor()
        c.execute('''
            INSERT INTO weather (city, main, temp, feels_like, dt)
            VALUES (?, ?, ?, ?, ?)
        ''', (city, data['weather'][0]['main'], data['main']['temp'] - 273.15, data['main']['feels_like'] - 273.15, data['dt']))
        conn.commit()
        conn.close()
    except KeyError as e:
        print(f"KeyError: {e} in data: {data}")



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/daily_summary')
def daily_summary():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('''
        SELECT city, date(dt, 'unixepoch'), AVG(temp), MAX(temp), MIN(temp), MAX(main)
        FROM weather
        GROUP BY city, date(dt, 'unixepoch')
    ''')
    summary = c.fetchall()
    conn.close()
    return jsonify(summary)

@app.route('/alerts', methods=['POST'])
def alerts():
    threshold = request.json.get('threshold')
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('''
        SELECT city, temp, dt
        FROM weather
        WHERE temp > ?
        ORDER BY dt DESC
        LIMIT 2
    ''', (threshold,))
    recent_temps = c.fetchall()
    print(f"Recent temps: {recent_temps}")  # Log the recent temperatures
    conn.close()
    if len(recent_temps) == 2 and recent_temps[0][1] > threshold and recent_temps[1][1] > threshold:
        alerts_data = [{'city': row[0], 'temp': row[1], 'dt': row[2]} for row in recent_temps]
        return jsonify({'alert': 'Temperature exceeded threshold for two consecutive updates!', 'data': alerts_data})
    else:
        return jsonify({'alert': 'No alert', 'data': []})


@app.route('/historical_trends')
def historical_trends():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    c.execute('''
        SELECT date(dt, 'unixepoch') as date, AVG(temp) as avg_temp
        FROM weather
        GROUP BY date
        ORDER BY date DESC
        LIMIT 30  -- Last 30 days
    ''')
    trends = c.fetchall()
    conn.close()
    return jsonify([{"date": row[0], "avg_temp": row[1]} for row in trends])

if __name__ == '__main__':
    init_db()
    server_thread = threading.Thread(target=fetch_weather_data)
    server_thread.daemon = True
    server_thread.start()
    
    try:
        socketio.run(app,host="0.0.0.0",port=3000,debug=True,allow_unsafe_werkzeug=True)
    except KeyboardInterrupt:
        print("Shutting down server...")
        server_thread.join()  # Ensure threads are properly closed

