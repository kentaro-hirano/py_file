from selenium  import webdriver # webdriveインポート

browser = webdriver.Chrome()
browser.get("https://b.hatena.ne.jp/search/tag?q=COVID-19&sort=recent&users=500&safe=on") # URL取得

art_title_names = browser.find_elements_by_class_name('centerarticle-entry-title') #記事タイトル取得
art_titles = []
for art_title_name in art_title_names:
  value = art_title_name.text
  art_titles.append(value)   

bm_user_elements = browser.find_elements_by_class_name('centerarticle-users') # ブックマーク数取得
bm_users = []
for bm_user_element in bm_user_elements:
  value = bm_user_element.text.replace('users', '') # users消去
  bm_users.append(value)

post_date_elements = browser.find_elements_by_class_name('entry-contents-date') # 投稿日取得
post_dates = []
for post_date_element in post_date_elements:
    value = post_date_element.text
    post_dates.append(value)

import pandas as pd # pandasインポート

df = pd.DataFrame()
df['タイトル'] = art_titles
df['ブックマーク数'] = bm_users
df['投稿日'] = post_dates
df['詳細リンク'] = title_links
df.to_csv('はてなブックマーク.csv', index=False) # csvに書き出し