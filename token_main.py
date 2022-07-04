import news_scrap as ns
import file_manager as fm
from eunjeon import Mecab

file_path = "C:/Users/차태진/Desktop/dev/python/tokenizer-exam/data/KBS.json"
file_path2 = "C:/Users/차태진/Desktop/dev/python/tokenizer-exam/data/KBS_new_bodies.json"
news_list = fm.load_json(file_path)

bodies = ns.get_news_bodies_by_news_list(news_list)

fm.save_to_json(file_path2, bodies)

bodies = fm.load_json(file_path2)

# 형태소 분석

m = Mecab()
rst = m.morphs(bodies[0]['body'])
rst = m.nouns(bodies[0]['body'])

rst = m.pos(bodies[0]['body'])
from collections import Counter

noun_adj_list = []
print(rst)

# tag가 명사이거나 형용사인 단어들만 noun_adj_list에 넣어준다.
for word, tag in rst:
    if tag in ['NNG' , 'NNP', 'VV', 'VA']: 
        noun_adj_list.append(word)

# 가장 많이 나온 단어부터 40개를 저장한다.
counts = Counter(noun_adj_list)
tags = counts.most_common(40) 

from wordcloud import WordCloud
# WordCloud를 생성한다.
# 한글을 분석하기위해 font를 한글로 지정해주어야 된다. macOS는 .otf , window는 .ttf 파일의 위치를
# 지정해준다. (ex. '/Font/GodoM.otf')
wc = WordCloud(font_path="C:/Windows/Fonts/MALGUN.TTF",background_color="white", max_font_size=60)
cloud = wc.generate_from_frequencies(dict(tags))

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
plt.axis('off')
plt.imshow(cloud)
plt.show()

# 30개 정도

cloud.to_file('test.jpg')