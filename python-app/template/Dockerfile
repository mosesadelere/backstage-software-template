FROM python:3.12-alpine

RUN mkdir -p /src

COPY requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

COPY ./src /src

CMD ["python", "/src/app.py"]
