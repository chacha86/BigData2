from ast import keyword
import json

dic1 = {"col1" : "val3", "col2" : "val10"}
dic2 = {"col1" : "val4", "col2" : "val11"}
dic3 = {"col1" : "val5", "col2" : "val12"}

jarr = [dic1, dic2, dic3]

keywords = []
with open('C:/Users/차태진/Desktop/dev/python/tokenizer-exam/data/test.json', 'r', encoding='utf-8-sig') as f :
    keywords = json.load(f)
    print(keywords)

keywords.append(dic1)
keywords.append(dic2)
keywords.append(dic3)

with open('C:/Users/차태진/Desktop/dev/python/tokenizer-exam/data/test.json', 'w', encoding='utf-8-sig') as f :
    json.dump(keywords, f, ensure_ascii=False, indent=4)



# dic2 = {"col1" : "val5", "col2" : "val8"}
# dic3 = {"col1" : "val6", "col2" : "val9"}

# jarr = [dic1, dic2, dic3]

# with open('C:/Users/차태진/Desktop/dev/python/tokenizer-exam/data/test.json', 'a', encoding='utf-8-sig') as f :
#     json.dump(jarr, f, ensure_ascii=False, indent=4)


# with open('C:/Users/차태진/Desktop/dev/python/tokenizer-exam/data/test.json', 'r', encoding='utf-8-sig') as f :
#     jarr = json.load(f)

#     print(jarr)
