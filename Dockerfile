FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app

CMD ["uvicorn", "sicei:app", "--host", "0.0.0.0", "--port", "8000"]