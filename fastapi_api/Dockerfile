FROM python:3.11-slim-buster

WORKDIR /app

COPY fastapi_api/requirements.txt .
RUN pip install -r requirements.txt

COPY ../ .
COPY ../utils/ ./utils/
COPY ../data/ ./data/

EXPOSE 8000

CMD ["uvicorn", "fastapi_api.main_api:app", "--host", "0.0.0.0", "--port", "8000"]