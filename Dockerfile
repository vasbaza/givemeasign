FROM python:3

COPY . /myapp
WORKDIR ./app

RUN pip freeze > requirements.txt

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD python app.py