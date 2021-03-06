FROM python:3

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install -r ./app/requirements.txt

CMD python /app/app/app.py