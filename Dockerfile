FROM python:3

COPY . /app

RUN pip freeze > requirements.txt

RUN pip install --upgrade pip && \
    pip install -r app/requirements.txt \
    pip install flask \
    pip install pymongo \
    pip install dnspython

CMD python /app/app/app.py