FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

COPY . /app
WORKDIR /app
RUN ls /app
RUN pip install -r requirements.txt
RUN chmod +x /app/startup.sh
ENTRYPOINT /app/startup.sh