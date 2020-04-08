# 名前に反応してDBからデータを取得、クラスの形に突っ込む
# mysqlかな
#　以下練習
#import mysql.connector as mydb

#conn = mydb.connect(
    #host='127.0.0.1',
    #port='3306',
    #user='root',
    #password='w9478zqh',
    #db='sample1')
#conn.ping(reconnect=True)
#cur = conn.cursor()

#参考サイト：https://lets-hack.tech/programming/languages/python/beautifulsoup/
from pymongo import MongoClient
import pymongo


client = MongoClient('localhost', 27017)
db = client.pokemon
collection = db.pokedb

#for i in collection.find({"a": {'$gte': 100}}).sort('s', pymongo.DESCENDING).limit(5):
    #print(i)



attacker = collection.find_one({'name': 'ドラパルト'})
a = ((attacker['a'] * 2 + 31 + (252) / 4) * 50 / 100 + 5) * 1.0  # attackerの(((race*2)+individual+(effort/2))*50/100+5)*personality

defender = collection.find_one({'name': 'ミミッキュ'})
h = (defender['h'] * 2 + 31 + (252) / 4) * 50 / 100 + 50 + 10  # defenderの((race*2)+individual+(effort/2))*50/100+50+10
b = ((defender['b'] * 2 + 31 + (252) / 4) * 50 / 100 + 5) * 1.0  # defenderの(((race*2)+individual+(effort/2))*50/100+5)*personality

print(attacker['name'], a)
print(defender['name'], h, b)