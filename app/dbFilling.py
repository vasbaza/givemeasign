import ssl
from random import randint

from pymongo import MongoClient
from pprint import pprint

client = MongoClient('mongodb+srv://vasbaza:butterfly@givemeasign.rs2mm.mongodb.net/test', ssl_cert_reqs=ssl.CERT_NONE)
db = client.signs

sign1 = {
    "sign": "Тебе нужна заколка для волос. Если у тебя нет волос, подари её своему волосатому другу"
}

sign2 = {
    "sign": "Срочно выпей стакан молока! Тебе нельзя молоко? В таком случае, брось эту затею..."
}

sign3 = {
    "sign": "Птички летают, букашки ползают, кроты копают, а ты что делаешь?..."
}

sign4 = {
    "sign": "Кажется, нам с тобой нужно побеседовать! (о ком ты подумал, прочитав это?)"
}

sign5 = {
    "sign": "Решение проблемы кроется в летающих коровах"
}

sign6 = {
    "sign": "Посмотри на небо, вон то облако ничего не напоминает? А отсутсвие облаков ни о чем не говорит?"
}

sign7 = {
    "sign": "Раз, два, три, четыре, пять, я иду тебя искать..."
}

sign8 = {
    "sign": "А что спрятано у тебя в карманцах? Думаю, об этом не стоит всем рассказывть"
}

sign9 = {
    "sign": "Летит лебедь, а за ним чайка, а за ним сойка... Постойте, а что из этого выйдет?"
}

sign10 = {
    "sign": "Не стоит раздувать из мухи слона, ведь лучше надуть воздушный шарик и побить этим шариком кого-нибудь бесячего"
}


db.reviews.insert_many([sign1, sign2, sign3, sign4, sign5, sign6, sign7, sign8, sign9, sign10])
