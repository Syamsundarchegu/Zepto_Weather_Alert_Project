# Use the latest Python runtime as a parent image
# Replace with the latest version if there's a newer one
FROM python:3.12.4

# Set environment variables

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# Replace with your actual API key
ENV API_KEY=your_api_key

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["flask", "run"]
