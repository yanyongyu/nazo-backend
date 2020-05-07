FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install pyjwt python-multipart sqlalchemy databases alembic -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

COPY ./nazo_backend /app/nazo_backend