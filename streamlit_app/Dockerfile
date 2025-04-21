FROM python:3.12

WORKDIR /app

COPY streamlit_app/requirements.txt .
RUN pip install -r requirements.txt

COPY streamlit_app/ .
COPY ../utils/ ./utils/
COPY ../data/ ./data/

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "main.py", "--server.address=0.0.0.0", "--server.port=8501"]