FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

ARG GIT_BRANCH
ARG BUILD_NUMBER

LABEL branch=${GIT_BRANCH}
LABEL build=${BUILD_NUMBER}

COPY ./app /app

CMD ["uvicorn", "sicei:app", "--host", "0.0.0.0", "--port", "8000"]

