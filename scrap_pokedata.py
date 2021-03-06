import requests
from urllib.parse import urljoin
from pathlib import Path, PurePath
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

# 覚える技判定用に技リスト読み込み
weapon_path = PurePath.joinpath(Path.cwd(), '技一覧.csv')
weapon_list = pd.read_csv(weapon_path, encoding='utf_8_sig', index_col=0)

# 日本語でスクレイプしたタイプを数字に変換するための表
type_num = {'ほのお': 1, 'みず': 2, 'むし': 3, 'あく': 4, 'ドラゴン': 5, 'でんき': 6, 'フェアリー': 7, 'かくとう': 8, 'ひこう': 9,
            'ゴースト': 10, 'くさ': 11, 'じめん': 12, 'こおり': 13, 'ノーマル': 14, 'どく': 15, 'エスパー': 16, 'いわ': 17,
            'はがね': 18, '': 19}
cate_num = {'物理': 0, '特殊': 1, '変化': 2}

main_url = 'https://yakkun.com/swsh/zukan/'
# seleniumでアクセス
options = Options()
options.add_argument('--headless')
try:
    driver = webdriver.Chrome(r'C:/Users/g2945/chromedriver/chromedriver', options=options)
except:
    driver = webdriver.Chrome(r'', options=options)
driver.get(main_url)
# 全国図鑑へ遷移
sort = driver.find_element_by_xpath('/html/body/div/div[3]/div[1]/div[6]/ul[3]/li[3]')
sort.click()
# html取得してBS4へ投げる
html = driver.page_source.encode('utf-8')
driver.quit()
soup = bs(html, 'html.parser')
# data=リンクからURL生成
data = soup.select('#contents > div.pokemon_list_box > ul.pokemon_list > li > a')
urls = [urljoin(main_url, _url.get('href')) for _url in data]

save_path = PurePath.joinpath(Path.cwd(), '種族値.csv')

df = pd.DataFrame()
# 詳細ページにアクセス→スクレイプ
for i, url in enumerate(urls):
    r = requests.get(url)
    soup2 = bs(r.content, 'html.parser')

    name = soup2.select('.head > th[colspan="2"]')[0].text
    # 名前がすでにある場合はスキップ
    if save_path.exists() and name in list(data['name']):
        continue
    # error があった場合は空欄で対処
    try:
        li_box = [s.find_all('li') for s in soup2.select('.center') if not s.find_all('li') == []]
        weight = float(li_box[0][0].text.replace('kg', ''))
    except:
        weight = ''
    try:
        h = int(soup2.select('#stats_anchor > table > tr:nth-child(2) > td.left')[0].text)
    except:
        h = ''
    try:
        a = int(soup2.select('#stats_anchor > table > tr:nth-child(3) > td.left')[0].text)
    except:
        a = ''
    try:
        b = int(soup2.select('#stats_anchor > table > tr:nth-child(4) > td.left')[0].text)
    except:
        b = ''
    try:
        c = int(soup2.select('#stats_anchor > table > tr:nth-child(5) > td.left')[0].text)
    except:
        c = ''
    try:
        d = int(soup2.select('#stats_anchor > table > tr:nth-child(6) > td.left')[0].text)
    except:
        d = ''
    try:
        s = int(soup2.select('#stats_anchor > table > tr:nth-child(7) > td.left')[0].text)
    except:
        s = ''
    try:
        type_ = li_box[1]
        type1 = type_[0].find('img').get('alt')
        type2 = ''
        if len(type_) > 1:
            type2 = type_[1].find('img').get('alt')
    except:
        type1 = ''
        type2 = ''
    try:
        weapon_table = soup2.select('.move_name_cell')
        wl = [t.text.replace('[遺伝経路]', '') for t in weapon_table]
        # 削除技は技一覧で照会してもはじかれるよう設定
        wl = [w for w in wl if w in weapon_list.columns]
    except:
        wl = []

    poke = {'name': name, 'type1': type_num[type1], 'type2': type_num[type2], 'weight': weight,
            'h': h, 'a': a, 'b': b, 'c': c, 'd': d, 's': s, 'weapon': wl}

    df = df.append(poke, ignore_index=True)
# 進捗表示
    prog = round((i + 1) / len(urls) * 100, 2)
    if 4.98 < prog < 5.11:
        print(round(prog), '%完了', sep='')
    elif 9.98 < prog < 10.11:
        print(round(prog), '%完了', sep='')
    elif 14.98 < prog < 15.11:
        print(round(prog), '%完了', sep='')
    elif 19.98 < prog < 20.11:
        print(round(prog), '%完了', sep='')
    elif 24.98 < prog < 25.11:
        print(round(prog), '%完了', sep='')
    elif 29.98 < prog < 30.11:
        print(round(prog), '%完了', sep='')
    elif 34.98 < prog < 35.11:
        print(round(prog), '%完了', sep='')
    elif 39.98 < prog < 40.11:
        print(round(prog), '%完了', sep='')
    elif 44.98 < prog < 45.11:
        print(round(prog), '%完了', sep='')
    elif 49.98 < prog < 50.11:
        print(round(prog), '%完了', sep='')
    elif 54.98 < prog < 55.11:
        print(round(prog), '%完了', sep='')
    elif 59.98 < prog < 60.11:
        print(round(prog), '%完了', sep='')
    elif 64.98 < prog < 65.11:
        print(round(prog), '%完了', sep='')
    elif 69.98 < prog < 70.11:
        print(round(prog), '%完了', sep='')
    elif 74.98 < prog < 75.11:
        print(round(prog), '%完了', sep='')
    elif 79.98 < prog < 80.11:
        print(round(prog), '%完了', sep='')
    elif 84.98 < prog < 85.11:
        print(round(prog), '%完了', sep='')
    elif 89.98 < prog < 90.11:
        print(round(prog), '%完了', sep='')
    elif 94.98 < prog < 95.11:
        print(round(prog), '%完了', sep='')
    elif prog == 100:
        print(round(prog), '%完了', sep='')

df.to_csv(save_path, encoding='utf_8_sig')
