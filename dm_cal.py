import pokemon_db_connect

attacker = # ポケモンDBから種族値引っ張ってくる
a = # attackerの(((race*2)+individual+(effort/2))*50/100+5)*personality
skill = # ポケモンDBから技情報引っ張てくる
defenser = # DBから種族値引っ張ってくる
h = # defenserの((race*2)+individual+(effort/2))*50/100+50+10
b = # defenserの(((race*2)+individual+(effort/2))*50/100+5)*personality

width = {s: 1, w: 0.75}# シングル1 or ダブル0.75
weather = # 天候補正　晴れ　雨　砂
critical　=  1.5
random_num = [0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1]# 0.85~1.00 の16段階
type = {match: 1.5, discord: 1}# 一致かどうか 1 1.5
compatibility = # skillとdefenderの相性　0 0.25 0.5 1 2 4
burn =  0.5
m = (wall * sniper * colorgogle * mof * mhalf * mfilter * exbelt * lifeorb * choiceitem * berry)

orgin_dmg = ((22 * skill * a / b) / 50 + 2) * width{} * weather * critical * type * compatibility * burn * m

dmg = [origin_dmg * x for x in random_num]