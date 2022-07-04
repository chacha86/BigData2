from unittest import result
import news_scrap as ns
import file_manager as fm
from konlpy.tag import Okt


def get_item_list(bodies) :
    
    ok = Okt()
    result_list = []
    for i in range(len(bodies)) :
        rst = ok.pos(bodies[i]['body'])

        keyword_list = []

        from collections import Counter

        for word, tag in rst:
            if tag in ['NNG' , 'NNP', 'VV', 'VA']: 
                keyword_list.append(word)

        counts = Counter(keyword_list)

        item_list=[]
        for item in counts.items() :
            keyword = {
                'nid' : bodies[i]['nid'],
                'word' : item[0],
                'cnt' : item[1],
                'tag' : tag
            }
            item_list.append(keyword)
        result_list.extend(item_list)
    return result_list

# file_path = "C:/Users/차태진/Desktop/dev/python/tokenizer-exam/data/KBS.json"
file_path2 = "C:/Users/차태진/Desktop/dev/python/tokenizer-exam/data/KBS_new_bodies.json"
# news_list = fm.load_json(file_path)

# bodies = ns.get_news_bodies_by_news_list(news_list)

# fm.save_to_json(file_path2, bodies)

bodies = fm.load_json(file_path2)

print(bodies)
# 형태소 분석

item_list = get_item_list(bodies)
file_path3 = "C:/Users/차태진/Desktop/dev/python/tokenizer-exam/data/news_keyword.json"

fm.save_to_json(file_path3, item_list)

