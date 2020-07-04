import ssl, os
from random import randint

from pymongo import MongoClient
from pprint import pprint

client = MongoClient(os.environ.get('DB_STRING'), ssl_cert_reqs=ssl.CERT_NONE)
db = client.signs

cur = db.reviews.find()
objects_from_db = []


def from_db_to_list(cur):
    for i in cur:
        objects_from_db.append(i)
    return objects_from_db


def look_for_sign(cur):
    objects_from_db = from_db_to_list(cur)
    random_int = randint(0, 9)
    dict = objects_from_db[random_int]
    sign = dict['sign']
    return sign
