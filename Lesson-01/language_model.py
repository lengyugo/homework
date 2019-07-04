import pandas as pd
import re
import jieba
from functools import reduce
from operator import add,mul
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

filename = 'F:/NLP/datasource-master/datasource/sqlResult_1558435.csv'
content = pd.read_csv(filename,encoding='gb18030')
#print(content.head())

articles = content['content'].tolist()
#print(len(articles))

def token(string):
    return re.findall('\w+',string)
#print(''.join(token(articles[110])))

article_clean = [''.join(token(str(a))) for a in articles]

with open('clean_data.txt','w') as f:
    for a in article_clean:
        f.write(a + '\n')
#print(len(article_clean))

def cuting(string):
    return list(jieba.cut(string))

##直接切词

# clean_data = [cuting(string) for string in article_clean]
#
Token = []
# Token = reduce(add,clean_data)

##保存到文件中在切词
#Token = reduce(add,cuting(article_clean))
for i,line in enumerate((open('clean_data.txt'))):
#for i ,line in enumerate(article_clean):
    if i % 100 == 0: print(i)

    Token += cuting(line)

words_count = Counter(Token)

#print(words_count.most_common(100))

# frequiences = [f for w,f in words_count.most_common(100)]
# x = [i for i in range(100)]
# #plt.plot(x,frequiences)
#
# plt.plot(x,np.log(frequiences))
# plt.show()

def prob_1(word):
    return words_count[word] / len(Token)

TOKEN = [str(t) for t in Token]
TOKEN_2_GRAM = [''.join(TOKEN[i:i+2]) for i in range(len(TOKEN[:-2]))]
words2_count = Counter(TOKEN_2_GRAM)

def prob_2(word1,word2):
    if word1 + word2 in words2_count:
        return words2_count[word1 + word2] / len(TOKEN_2_GRAM)
    else:
        return 1 / len(TOKEN_2_GRAM)

def get_probablity(sentence):
    words = cuting(sentence)
    sentence_pro = 1

    for i,word in enumerate(words[:-1]):

        next_ = words[i+1]
        probability = prob_2(word,next_)
        sentence_pro *= probability
    return sentence_pro

print(get_probablity('小明今天抽奖抽到一台苹果手机'))
print(get_probablity('小明今天抽奖抽到一架波音飞机'))

need_compared = [
    "今天晚上请你吃大餐，我们一起吃日料 明天晚上请你吃大餐，我们一起吃苹果",
    "真事一只好看的小猫 真是一只好看的小猫",
    "今晚我去吃火锅 今晚火锅去吃我",
    "洋葱奶昔来一杯 养乐多绿来一杯"
]

for s in need_compared:
    s1, s2 = s.split()
    p1, p2 = get_probablity(s1), get_probablity(s2)

    better = s1 if p1 > p2 else s2

    print('{} is more possible'.format(better))
    print('-' * 4 + ' {} with probility {}'.format(s1, p1))
    print('-' * 4 + ' {} with probility {}'.format(s2, p2))








