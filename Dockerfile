FROM python:3.9.0-alpine
LABEL maintainer="David Leon <david.leon.m@gmail.com>"

# Copy the application folder by folder because .gitignore does not work for me to skip unit tests
COPY WeatherStationSensorsReader/app /WeatherStationSensorsReader/app
COPY WeatherStationSensorsReader/controllers /WeatherStationSensorsReader/controllers
COPY WeatherStationSensorsReader/dao /WeatherStationSensorsReader/dao
COPY WeatherStationSensorsReader/health_check /WeatherStationSensorsReader/health_check
COPY WeatherStationSensorsReader/main /WeatherStationSensorsReader/main
COPY WeatherStationSensorsReader/sensors /WeatherStationSensorsReader/sensors
COPY WeatherStationSensorsReader/requirements.txt /WeatherStationSensorsReader/requirements.txt

# Install needed packages for Python libraries
RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev

# Install Python references
RUN pip install --upgrade pip
RUN pip install -r /WeatherStationSensorsReader/requirements.txt

# Change working directory to the app binaries
WORKDIR /WeatherStationSensorsReader

# Configure the health check command
HEALTHCHECK CMD python -u -m health_check.health_check || exit 1

# Start the application
ENTRYPOINT ["python", "-u", "-m", "app.app"]