FROM python:3.6-slim

MAINTAINER Kelvin Tay <kelvintaywl@gmail.com>

WORKDIR /lag

COPY server.py .
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD python server.py --port $PORT
