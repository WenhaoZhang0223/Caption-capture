import requests #发起 HTTP 请求
from bs4 import BeautifulSoup
import snownlp
from collections import Counter

class DanMu(object):  #定义类
    def __init__(self): #__init__ 方法在创建类的实例时被调用
        self.headers = {  #初始化header
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
        }
        self.url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=1275558615' #获取弹幕信息

    # 获取网页信息
    def get_html(self):
        response = requests.get(self.url, headers=self.headers)  #发送http get请求
        html = response.content.decode('utf-8')
        return html

    # 保存弹幕
    def get_info(self):
        html = self.get_html()
        soup = BeautifulSoup(html, 'lxml') #用beautifulsoup解析 HTML 文档
        file = open('iphone 15 测评弹幕.txt', 'w', encoding='utf-8')
        for d in soup.find_all(name='d'):
            danmu = d.string
            file.write(danmu)
            file.write('\n')

if __name__ == '__main__':
    danmu = DanMu()
    print('正在解析，开始爬取弹幕中。。。。。')
    danmu.get_info()

# snownlp情感分析:
source = open("C:\\Users\\Aoteman\\Desktop\\Code\\wang_luo_pa_chong\\pythonProject\\iphone 15 测评弹幕.txt", "r", encoding="utf-8")
line = source.readlines()

senti =[]
for i in line:
    s = snownlp.SnowNLP(i)
    #print (s.sentiments)
    senti.append(s.sentiments)

import matplotlib.pyplot as plt
import numpy as np
x =np.array(range(len(senti)))
y =np.array(senti)
plt.scatter(x,y)
plt.show ()

s1 = snownlp.SnowNLP("C:\\Users\\Aoteman\\Desktop\\Code\\wang_luo_pa_chong\\pythonProject\\iphone 15 测评弹幕.txt")
print(s1.sentiments)

# 计算高频词：
filename = "C:\\Users\\Aoteman\\Desktop\\Code\\wang_luo_pa_chong\\pythonProject\\iphone 15 测评弹幕.txt"
with open(filename, "r", encoding="utf-8") as source:
    lines = source.readlines()

# 计算高频词
words = " ".join(lines).split()
word_counter = Counter(words)

# 打印高频词
top_words = 10  # 设置要打印的前几个高频词
selected_words = [word for word, _ in word_counter.most_common(top_words)]

# 打印高频词
print(f"\nTop {top_words} 高频词:")
for word, count in word_counter.most_common(top_words):
    print(f"{word}: {count} 次")

#生成高频词文档
output_filename = "high_frequency_words1.txt"
with open(output_filename, "w", encoding="utf-8") as output_file:
    output_file.write("\n".join(selected_words))

print(f"\n高频词已写入文件: {output_filename}")