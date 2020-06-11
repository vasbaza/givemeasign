FROM python:3

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip && \
    pip install flask

CMD python app.py
