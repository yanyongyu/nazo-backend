FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install pyjwt python-multipart sqlalchemy databases alembic

COPY ./nazo_backend /app/nazo_backend