from konlpy import jvm
from konlpy.tag import Okt 
from konlpy.tag import Kkma 
from eunjeon import Mecab

import os
from konlpy import utils


javadir = '%s%sjava' % (utils.installpath, os.sep)
args = [javadir, os.sep]
folder_suffix = ['{0}{1}open-korean-text-2.1.0.jar']
classpath = [f.format(*args) for f in folder_suffix]

print('javadir  : {}'.format(javadir))
print('os.sep   : {}'.format(os.sep))
print('classpath: {}'.format(classpath[0]))

# 형태소 분석해서 뭐할건데??
# 20대가 본 뉴스에서 가장 많이 언급된 명사
# 여자들이 본 뉴스에서 가장 많이 언급된 명사

m = Mecab()
rst = m.morphs("안녕하세요 저는 홍길도입니다. 눈이 좀 아푸네요")
rst2 = m.nouns("안녕하세요 저는 홍길도입니다. 눈이 좀 아푸네요")
print(rst2)