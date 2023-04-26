"""
    @author: yaunsine
    生成词云图
"""
import jieba
import wordcloud
import pandas as pd
import datetime

file_name = "paperExcel/Gan.csv"
user_dict_path = "config\\custom_userdict.txt"
cut_temp_path = "temp\\cut_temp.txt"
stop_file_path = "config\\stopwords.txt"

search_content = file_name.split("/")[1].split(".")[0]
data = pd.read_csv(file_name)
s = "".join(data['title'])
s = s.replace("\n", " ")
del data
with open(user_dict_path, mode="r", encoding="utf-8") as fp:
    lines = fp.readlines()
    for line in lines:
        line = line.replace("\n", "")
        jieba.add_word(line)

jieba.load_userdict(user_dict_path)
ls = jieba.lcut(s) # 生成分词列表
with open(cut_temp_path, encoding="utf-8", mode="w") as fp:
    fp.writelines(str(ls))

text = ' '.join(ls) # 连接成字符串


with open(stop_file_path, encoding="utf-8") as fp:
    s = fp.readlines()
s = list(map(lambda x: x.replace('\n',''), s))
wc = wordcloud.WordCloud(font_path="msyh.ttc",
                         width = 1000,
                         height = 700,
                         background_color='white',
                         max_words=100,stopwords=s)
# msyh.ttc电脑本地字体，写可以写成绝对路径
wc.generate(text) # 加载词云文本

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
wc.to_file(f"imgs//cloudword_{search_content}{time_stamp}.png".replace(":", "_")) # 保存词云文件
