FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

ENTRYPOINT  ["streamlit", "run", "main.py", "--server.address=0.0.0.0", "--server.port=8501"]
