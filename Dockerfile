FROM python:3.12.3-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY .e.json .
COPY get_weather.py .
COPY handlers.py .
COPY main.py .
COPY openweathermapapi.py .
COPY text.py .
CMD ["python", "main.py"]