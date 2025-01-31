FROM python:3.10-slim

WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . . 

RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python", "main.py"]
