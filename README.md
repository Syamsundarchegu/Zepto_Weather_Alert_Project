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
    git clone https://github.com/Syamsundarchegu/Zepto_Weather_Alert_Project.git

    ```

2. **Create a virtual environment**
    ```bash
<<<<<<< HEAD
    conda create -name <environment_name> #For creating a virtual environment
    conda activate <environment_name>  #For activating the virtual environment
    conda deacity <environment_name>  #For deactivating the virtual environment
=======
    conda create -name <env-name>
    conda activate<env-name>
    conda deactivate
>>>>>>> 9526b9047aab327c0b0727111214e007cdd8f96c
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
    Open your web browser and go to `http://127.0.0.1:3000`.


### Docker Setup(Optional)
1. **Build the Docker image**
    ```bash
<<<<<<< HEAD
    docker build -t -p <username>/<image_name>:latest .
    docker run -d <username>/<image_name>:latest
    docker ps -a
    docker logs <container_object>
=======
    docker build -t <username>/<image-name>:latest .
>>>>>>> 9526b9047aab327c0b0727111214e007cdd8f96c
    ```

2. **Run the Docker container**
    ```bash
<<<<<<< HEAD
    docker run -d <username>/<image_name>:latest
=======
    docker run -t -p 3000:3000 <username>/<image-name>:latest
>>>>>>> 9526b9047aab327c0b0727111214e007cdd8f96c
    ```
## Maditory Step
Access the application at `http://127.0.0.1:3000`.


### Design Choices
- **Flask**: Chosen for its simplicity and ease of use to create a web server.
- **SQLite**: Lightweight database suitable for development and quick prototyping.
- **OpenWeatherMap API**: Reliable and comprehensive weather data provider.
- **Docker**: Ensures the application can run consistently across different environments.
