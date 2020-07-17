import pandas as pd
import math
from pathlib import Path, PurePath

poke_path = Path(r'C:\Users\g2945\Desktop\jupyter\DMcal\種族値.csv')
weapon_path = Path(r'C:\Users\g2945\Desktop\jupyter\DMcal\技一覧.csv')


df = pd.read_csv(poke_path, encoding='utf_8_sig', index_col=0)
weapon = pd.read_csv(weapon_path, encoding='utf_8_sig', index_col=0)

type_list  =  {
                'fire':{'normal':1, 'fire':1, 'water':1, 'electric':1, 'grass':1, 'ice':1, 'fighting':1, 'poison':1, 'ground':1,
                       'flying':1, 'psychic':1, 'bug':1, 'rock':0.5, 'ghost':0, 'dragon':1, 'dark':1, 'steel':0.5, 'fairy':1},
               'water':{'normal':1, 'fire':2, 'water':0.5,'electric':1, 'grass':0.5, 'ice':1, 'fighting':1, 'poison':1, 'ground':2.0,
                        'flying':1, 'psychic':1, 'bug':1, 'rock':2.0, 'ghost':1, 'dragon':0.5, 'dark':1, 'steel':1, 'fairy':1},
               'bug':{'normal':1, 'fire':0.5, 'water':1, 'electric':1, 'grass':2.0, 'ice':1, 'fighting':0.5, 'poison':0.5, 'ground':1,
                      'flying':0.5, 'psychic':2, 'bug':1, 'rock':1, 'ghost':0.5, 'dragon':1, 'dark':2, 'steel':0.5, 'fairy':0.5},
               'dark':{'normal':1, 'fire':1, 'water':1, 'electric':1, 'grass':1, 'ice':1, 'fighting':0.5, 'poison':1, 'ground':1,
                       'flying':1, 'psychic':2, 'bug':1, 'rock':1, 'ghost':2, 'dragon':1, 'dark':0.5, 'steel':1, 'fairy':0.5},
               'dragon':{'normal':1, 'fire':1, 'water':1, 'electric':1, 'grass':1, 'ice':1, 'fighting':1, 'poison':1, 'ground':1,
                         'flying':1, 'psychic':1, 'bug':1, 'rock':1, 'ghost':1, 'dragon':2, 'dark':1, 'steel':0.5, 'fairy':0},
               'electric':{'normal':1, 'fire':1, 'water':2, 'electric':0.5, 'grass':0.5, 'ice':1, 'fighting':1, 'poison':1, 'ground':0,
                           'flying':2, 'psychic':1, 'bug':1, 'rock':1, 'ghost':1, 'dragon':0.5, 'dark':1, 'steel':1, 'fairy':1},
               'fairy':{'normal':1, 'fire':0.5, 'water':1, 'electric':1, 'grass':1, 'ice':1, 'fighting':2, 'poison':0.5, 'ground':1,
                        'flying':1, 'psychic':1, 'bug':1, 'rock':1, 'ghost':1, 'dragon':2 , 'dark':2, 'steel':0.5, 'fairy':1},
               'fighting':{'normal':2, 'fire':1, 'water':1, 'electric':1, 'grass':1, 'ice':2, 'fighting':1, 'poison':0.5, 'ground':1,
                           'flying':0.5, 'psychic':0.5, 'bug':0.5, 'rock':2, 'ghost':0, 'dragon':1, 'dark':2, 'steel':2, 'fairy':0.5},
               'flying':{'normal':1, 'fire':1, 'water':1, 'electric':0.5, 'grass':2, 'ice':1, 'fighting':2, 'poison':1, 'ground':1,
                         'flying':1, 'psychic':1, 'bug':2, 'rock':0.5, 'ghost':1, 'dragon':1, 'dark':1, 'steel':0.5, 'fairy':1},
               'ghost':{'normal':0, 'fire':1, 'water':1, 'electric':1, 'grass':1, 'ice':1, 'fighting':1, 'poison':1, 'ground':1,
                        'flying':1, 'psychic':2, 'bug':1, 'rock':1, 'ghost':2, 'dragon':1, 'dark':0.5, 'steel':1, 'fairy':1},
               'grass':{'normal':1, 'fire':0.5, 'water':2, 'electric':1, 'grass':0.5, 'ice':1, 'fighting':1, 'poison':0.5, 'ground':2,
                        'flying':0.5, 'psychic':1, 'bug':0.5, 'rock':2, 'ghost':1, 'dragon':0.5, 'dark':1, 'steel':0.5, 'fairy':1},
               'ground':{'normal':1, 'fire':2, 'water':1, 'electric':2, 'grass':0.5, 'ice':1, 'fighting':1, 'poison':2, 'ground':1,
                         'flying':0, 'psychic':1, 'bug':0.5, 'rock':2, 'ghost':1, 'dragon':1, 'dark':1, 'steel':2, 'fairy':1},
               'ice':{'normal':1, 'fire':0.5, 'water':0.5, 'electric':1, 'grass':2, 'ice':0.5, 'fighting':1, 'poison':1, 'ground':2,
                      'flying':2, 'psychic':1, 'bug':1, 'rock':1, 'ghost':1, 'dragon':2, 'dark':1, 'steel':0.5, 'fairy':1},
               'normal':{'normal':1, 'fire':1, 'water':1, 'electric':1, 'grass':1, 'ice':1, 'fighting':1, 'poison':1, 'ground':1,
                         'flying':1, 'psychic':1, 'bug':1, 'rock':0.5, 'ghost':0, 'dragon':1, 'dark':1, 'steel':0.5, 'fairy':1},
               'poison':{'normal':1, 'fire':1, 'water':1, 'electric':1, 'grass':2, 'ice':1, 'fighting':1, 'poison':0.5, 'ground':0.5,
                         'flying':1, 'psychic':1, 'bug':1, 'rock':0.5, 'ghost':0.5, 'dragon':1, 'dark':1, 'steel':0, 'fairy':2},
               'psychic':{'normal':1, 'fire':1, 'water':1, 'electric':1, 'grass':1, 'ice':1, 'fighting':2, 'poison':2, 'ground':1,
                          'flying':1, 'psychic':0.5, 'bug':1, 'rock':1, 'ghost':1, 'dragon':1, 'dark':0, 'steel':0.5, 'fairy':1},
               'rock':{'normal':1, 'fire':2, 'water':1, 'electric':1, 'grass':1, 'ice':2, 'fighting':0.5, 'poison':1, 'ground':0.5,
                       'flying':2, 'psychic':1, 'bug':2, 'rock':1, 'ghost':1, 'dragon':1, 'dark':1, 'steel':0.5, 'fairy':1},
               'steel':{'normal':1, 'fire':0.5, 'water':0.5, 'electric':0.5, 'grass':1, 'ice':2, 'fighting':1, 'poison':1, 'ground':1,
                        'flying':1, 'psychic':1, 'bug':1, 'rock':2, 'ghost':1, 'dragon':1, 'dark':1, 'steel':0.5, 'fairy':2},
                'None':{'normal':1, 'fire':1, 'water':1, 'electric':1, 'grass':1, 'ice':1, 'fighting':1, 'poison':1, 'ground':1,
                        'flying':1, 'psychic':1, 'bug':1, 'rock':1, 'ghost':1, 'dragon':1, 'dark':1, 'steel':1, 'fairy':1}
              }

a_items = {'いのちのたま':1.3, 'こだわりハチマキ':1.5, 'こだわりメガネ':1.5, 'タイプ強化系':1.2,
           'たつじんのおび':1.2, 'ちからのハチマキ':1.1,'ものしりメガネ':1.1, 'ノーマルジュエル':1.3, 'ふといほね':2}

d_items = {'とつげきチョッキ':1.5, 'しんかのきせき':1.5, '半減きのみ':0.5, 'その他':1}

type_num = {'ほのお':1, 'みず':2, 'むし':3, 'あく':4, 'ドラゴン':5, 'でんき':6, 'フェアリー':7, 'かくとう':8, 'ひこう':9,
            'ゴースト':10, 'くさ':11, 'じめん':12, 'こおり':13, 'ノーマル':14, 'どく':15, 'エスパー':16, 'いわ':17,
            'はがね':18, '':19}

num_type = {1:'fire', 2:'water', 3:'bug', 4:'dark', 5:'dragon', 6:'electric', 7:'fairy', 8:'fighting', 9:'flying',
            10:'ghost', 11:'grass', 12:'ground', 13:'ice', 14:'normal', 15:'poison', 16:'psychic', 17:'rock', 18:'steel', 19:'None'}

per_list = {
    'いじっぱり':{'a':1.1, 'b':1, 'c':0.9, 'd':1, 's':1},
    'さみしがり':{'a':1.1, 'b':0.9, 'c':1, 'd':1, 's':1},
    'やんちゃ':{'a':1.1, 'b':1, 'c':1, 'd':0.9, 's':1},
    'ゆうかん':{'a':1.1, 'b':1, 'c':1, 'd':1, 's':0.9},
    'ずぶとい':{'a':0.9, 'b':1.1, 'c':1, 'd':1, 's':1},
    'わんぱく':{'a':1, 'b':1.1, 'c':0.9, 'd':1, 's':1},
    'のうてんき':{'a':1, 'b':1.1, 'c':1, 'd':0.9, 's':1},
    'のんき':{'a':1, 'b':1.1, 'c':1, 'd':1, 's':0.9},
    'ひかえめ':{'a':0.9, 'b':1, 'c':1.1, 'd':1, 's':1},
    'おっとり':{'a':1, 'b':0.9, 'c':1.1, 'd':1, 's':1},
    'うっかりや':{'a':1, 'b':1, 'c':1.1, 'd':0.9, 's':1},
    'れいせい':{'a':1, 'b':1, 'c':1.1, 'd':1, 's':0.9},
    'おだやか':{'a':0.9, 'b':1, 'c':1, 'd':1.1, 's':1},
    'おとなしい':{'a':1, 'b':0.9, 'c':1, 'd':1.1, 's':1},
    'しんちょう':{'a':1, 'b':1, 'c':0.9, 'd':1.1, 's':1},
    'なまいき':{'a':1, 'b':1, 'c':1, 'd':1.1, 's':0.9},
    'おくびょう':{'a':0.9, 'b':1, 'c':1, 'd':1, 's':1.1},
    'せっかち':{'a':1, 's':1.1, 'b':0.9, 'c':1, 'd':1},
    'ようき':{'s':1.1, 'b':1, 'c':1, 'd':1, 'a':0.9},
    'むじゃき':{'s':1.1, 'a':1, 'b':1, 'c':1, 'd':0.9},
}


# --------------------------------------------------
at_n = input('攻撃側(全角カタカナ)：')
at_per = input('性格：')
at = df[df['name'] == at_n]
at_type1 = num_type[int(at['type1'])]
at_type2 = num_type[int(at['type2'])]

eff_a = int(input('A努力値:'))
pe_a = per_list[at_per]['a']
a = int(at['a'])
a = math.floor(((a+31/2+eff_a/8)+5)*pe_a)

eff_c = int(input('C努力値:'))
pe_c = per_list[at_per]['c']
c = int(at['c'])
c = math.floor(((c+31/2+eff_c/8)+5)*pe_c)

# --------------------------------------------------
de_n = input('防御側(全角カタカナ)：')
de_per = input('性格：')
de = df[df['name'] == de_n]
de_type1 = num_type[int(de['type1'])]
de_type2 = num_type[int(de['type2'])]

eff_h = int(input('H努力値:'))
h = int(de['h'])
h = (h+31/2+eff_h/8)+60

eff_b = int(input('B努力値:'))
pe_b = per_list[de_per]['b']
b = int(de['b'])
b = math.floor(((b+31/2+eff_b/8)+5)*pe_b)

eff_d = int(input('D努力値:'))
pe_d = per_list[de_per]['d']
d = int(de['d'])
d = math.floor(((d+31/2+eff_d/8)+5)*pe_d)

# 技選択
w_name = input('技名(全角)：')
w_type = int(weapon[w_name][0])
w_type = num_type[w_type]
power = int(weapon[w_name][1])
hit = weapon[w_name][2]
pp = weapon[w_name][3]
cals = weapon[w_name][4]

# タイプ相性計算
com = type_list[w_type][de_type1] * type_list[w_type][de_type2]
# dmg計算：https://pokemon-wiki.net/%E3%83%80%E3%83%A1%E3%83%BC%E3%82%B8%E8%A8%88%E7%AE%97%E5%BC%8F#damageformula_detail
base_dmg = math.floor((math.floor(22 * (power*a/b))/50)+2)
ron = [0.85, 0.86, 0.87, 0.88, 0.89, 0.90, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.0]
dmg = [base_dmg * r for r in ron]
# 乱数計算後、タイプ一致判定しつつタイプ相性計算したものをリスト化
dmg = [dm * 1.5 * com if w_type==at_type1 or w_type==at_type2
       else dm * com  for dm in dmg]
# h_dmg = [(1-((h - dm)/h))*100 for dm in dmg]

print('攻撃側：', at_n, ' /　防御側：', de_n, sep='')
print('A実数値：', a, ' / B実数値:', b, sep='')
print('A性格補正：', pe_a, ' /　B性格補正：', pe_b, sep='')
print('技：', w_name, ' /　威力：', power, sep='')
print('----------------------------------------------------')
if int(h) - math.floor(min(dmg)) <= 0 :
    print('確定1発')
else:
    word = math.ceil( int(h) / math.floor(min(dmg)))
    print('確定{}発'.format(word))
print(math.floor(min(dmg)), '～', math.floor(max(dmg)), '/', int(h), sep='')
# print(round(min(h_dmg), 2), '% ～ ', round(max(h_dmg), 2), '%', sep='')
print(round((math.floor(min(dmg)) / int(h)) * 100, 2), '% ～ ', round((math.floor(max(dmg)) / int(h)) * 100, 2), '%', sep='')