FROM python:3

COPY . /app

WORKDIR /app

RUN pip freeze > requirements.txt

RUN pip install --upgrade pip && \
    pip install flask \
    pip install -r /requirements.txt


CMD python /app/app/app.py