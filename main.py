from isort import file
import journal_scrap as js
import news_scrap_sele as nss
import json
import file_manager as fm
import selenium_comment as sc

# 4. 뉴스는 news.json, 댓글은 comment.json으로 파일 저장
file_path = "C:/Users/차태진/Desktop/dev/python/tokenizer-exam/data/KBS.json"
news_list = fm.load_json(file_path)

print(news_list[0]['link'])

# for news in news_list :
    



