import journal_scrap as js
import news_scrap as ns
import json
import pandas as pd

# 1. 언론사 목록 가져오기
jlist = js.get_all_journal_list()
js.print_journal_list(jlist)

# 2. 언론사별 뉴스 가져오기
journal = jlist[0]
news_list = ns.get_new_list_by_journal(journal)
print(len(news_list))


