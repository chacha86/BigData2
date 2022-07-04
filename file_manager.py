import json
# dic = '''
# {
#     "age" : 20,
#     "name" : "hong",
#     "home" : "Daejeon"
# }
# '''
#dic['age']
#dic = json.loads(dic)

# dic1 = {"no" : 1, "name" : "hong"}
# dic2 = {"no" : 2, "name" : "lee"}

# dic_list = [dic1, dic2]

import os

def save_to_json(file_path, data) :
    origin = []
    if os.path.isfile(file_path) :
        with open(file_path, "r", encoding="utf-8-sig") as f1 :
            origin = json.load(f1)
        origin.extend(data)
        with open(file_path, "w", encoding='utf-8-sig') as f2 :
            json.dump(origin, f2, ensure_ascii=False)
    else :
        with open(file_path, "w", encoding='utf-8-sig') as f2 :
            json.dump(data, f2, ensure_ascii=False)
            


def load_json(file_path) :
    with open(file_path, "r", encoding='utf-8-sig') as f :
        news_list = json.load(f)
        return news_list


