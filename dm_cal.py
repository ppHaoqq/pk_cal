from pymongo import MongoClient
import pymongo

client = MongoClient('localhost', 27017)
db = client.pokemon
collection = db.pokedb

attacker = collection.find_one({'name': 'ドラパルト'})
a = ((attacker['a'] * 2 + 31 + (252) / 4) * 50 / 100 + 5) * 1.0  # attackerの(((race*2)+individual+(effort/2))*50/100+5)*personality
skill = # ポケモンDBから技情報引っ張てくる
defender = collection.find_one({'name': 'ミミッキュ'})
h = (defender['h'] * 2 + 31 + (252) / 4) * 50 / 100 + 50 + 10  # defenderの((race*2)+individual+(effort/2))*50/100+50+10
b = ((defender['b'] * 2 + 31 + (252) / 4) * 50 / 100 + 5) * 1.0  # defenderの(((race*2)+individual+(effort/2))*50/100+5)*personality

width = [1, 0.75]# シングル1 or ダブル0.75
weather = # 天候補正　晴れ　雨　砂
critical = 1.5
random_num = [0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1]# 0.85~1.00 の16段階
type = [1.5, 1]# 一致かどうか 1 1.5
compatibility = [0, 0.25, 0.5, 1, 2, 4]# skillとdefenderの相性　
burn =  0.5
m = (wall * sniper * colorgogle * mof * mhalf * mfilter * exbelt * lifeorb * choiceitem * berry)

origin_dmg = ((22* skill* a/ b) / 50+ 2)* width[0]* weather* critical* type[0]* compatibility[4]* burn* m

dmg = [origin_dmg* x for x in random_num]