FROM python:3.10

RUN mkdir app


WORKDIR /app
COPY . /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD uvicorn app:my_awesome_api --host 0.0.0.0 --port 8000