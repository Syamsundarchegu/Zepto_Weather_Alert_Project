# Weather Monitoring System

## Overview
This project is a real-time weather monitoring system that retrieves weather data from the OpenWeatherMap API, processes and analyzes the data, and provides summarized insights using rollups and aggregates. It includes alerting mechanisms and visualizations for daily summaries and historical trends.


## Build Instructions

### Prerequisites
- Docker or Podman
- Python 3.12.4
- Flask
- SQLite
- OpenWeatherMap API Key

### Setup
1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/weather_monitor.git
    cd weather_monitor
    ```

2. **Create a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**
    ```bash
    python app.py  # This will initialize the database
    ```

5. **Run the application**
    ```bash
    python app.py
    ```

6. **Access the application**
    Open your web browser and go to `http://127.0.0.1:5000`.


### Docker Setup(Optional)
1. **Build the Docker image**
    ```bash
    docker build -t weather_monitor .
    ```

2. **Run the Docker container**
    ```bash
    docker run -e API_KEY=your_openweathermap_api_key_here -p 5000:5000 weather_monitor
    ```
## Maditory Step
Access the application at `http://127.0.0.1:5000`.


### Design Choices
- **Flask**: Chosen for its simplicity and ease of use to create a web server.
- **SQLite**: Lightweight database suitable for development and quick prototyping.
- **OpenWeatherMap API**: Reliable and comprehensive weather data provider.
- **Docker**: Ensures the application can run consistently across different environments.
