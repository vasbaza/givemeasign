FROM python:3

COPY . /app

RUN pip freeze > requirements.txt

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD python /app/app/app.py