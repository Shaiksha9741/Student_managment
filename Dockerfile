FROM python:3.12-slim
RUN apt-get update && apt-get install -y libx11-6 libxext-dev libxrender-dev libxinerama-dev libxi-dev libxrandr libxcursor-devlibxts-dev libxtst-dev tk-dev python3-tk x11-apps && rm -rf /var/lib/apt/lists/*
ENV DISPLAY=${DISPLAY}
ENV XAUTHORITY=${XAUTHORITY}
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "login.py"]
