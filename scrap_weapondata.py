import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from pathlib import Path, PurePath

# 日本語でスクレイプしたタイプを数字に変換するための表
type_num = {'ほのお': 1, 'みず': 2, 'むし': 3, 'あく': 4, 'ドラゴン': 5, 'でんき': 6, 'フェアリー': 7, 'かくとう': 8,
            'ひこう': 9, 'ゴースト': 10, 'くさ': 11, 'じめん': 12, 'こおり': 13, 'ノーマル': 14, 'どく': 15, 'エスパー': 16,
            'いわ': 17, 'はがね': 18, '': 19}
cate_num = {'物理': 0, '特殊': 1, '変化': 2}

url = r'https://wiki.xn--rckteqa2e.com/wiki/%E3%82%8F%E3%81%96%E4%B8%80%E8%A6%A7_(%E7%AC%AC%E5%85%AB%E4%B8%96%E4%BB%A3)'
r = requests.get(url)
soup = bs(r.content, 'html.parser')
weapon_list = soup.find_all('tr')

dic = {}
for weapon in weapon_list:
    info = weapon.find_all('td')
    if len(info) < 1:
        continue
    name = info[0].text
    typ = info[1].text
    typ = type_num[typ]
    power = info[2].text
    hit = info[3].text
    pp = info[4].text
    cate = info[5].text.rstrip()
    try:
        cate = cate_num[cate]
    except:
        print(name, typ, power, hit, pp, cate)
    dic[name] = [typ, power, hit, pp, cate]

df = pd.DataFrame(dic)
save_path = PurePath.joinpath(Path.cwd(), '技一覧.csv')
df.to_csv(save_path, encoding='utf_8_sig')