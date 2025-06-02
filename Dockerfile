FROM python:3.12-slim
RUN apt-get update && apt-get install -y python3-tk x11-apps && rm -rf /var/lib/apt/lists/*
ENV DISPLAY=${DISPLAY}
ENV XAUTHORITY=${XAUTHORITY}
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "login.py"]
