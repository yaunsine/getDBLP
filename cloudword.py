import jieba
import wordcloud
import pandas as pd
# 读取文本
# with open("lhy_comments.txt",encoding="utf-8") as f:
#    s = f.read()
# print(s)
data = pd.read_csv('paperExcel\\Graphrecommend.csv')
s = "".join(data['title'])
s = s.replace("\n", " ")
del data
with open("config\\custom_userdict.txt", "r") as fp:
    lines = fp.readlines()
    for line in lines:
        line = line.replace("\n", "")
        jieba.add_word(line)

jieba.load_userdict("config\\custom_userdict.txt")
ls = jieba.lcut(s) # 生成分词列表
with open("cut_temp.txt", encoding="utf-8", mode="w") as fp:
    fp.writelines(str(ls))

text = ' '.join(ls) # 连接成字符串


stopwords = ["of","base","based", "for", "with", "Based on", "and"] # 去掉不需要显示的词
with open("config\\stopwords.txt", encoding="utf-8") as fp:
    s = fp.readlines()
s = list(map(lambda x: x.replace('\n',''), s))
print(s)
wc = wordcloud.WordCloud(font_path="msyh.ttc",
                         width = 1000,
                         height = 700,
                         background_color='white',
                         max_words=100,stopwords=s)
# msyh.ttc电脑本地字体，写可以写成绝对路径
wc.generate(text) # 加载词云文本
wc.to_file("cloudword.png") # 保存词云文件
