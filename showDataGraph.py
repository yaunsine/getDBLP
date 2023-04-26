import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import os
import datetime

file_name = "paperExcel/Gan.csv"
search_content = file_name.split("/")[1].split(".")[0]

data = pd.read_csv(file_name)
data = list(data['year'])
counter = Counter(data)


# 绘制条形图
x_values = list(counter.keys())
y_values = list(counter.values())

x_values, y_values = zip(*sorted(counter.items()))

plt.bar(x_values, y_values, color=(0.7, 0.7, 0.7))

# 绘制折线图
plt.plot(x_values, y_values, color='red', marker='o', linestyle='--')

# 添加轴标签和标题
plt.xlabel('Year')
plt.ylabel('Count')
plt.title(f'Frequency and Cumulative Frequency of {search_content}')
plt.xticks(list(range(min(x_values), max(x_values)+1, 1)))
plt.grid()

for x, y in zip(x_values, y_values):
    plt.text(x, y, str(y), ha='center', va='bottom', color='red')

# 保存图片到imgs目录下
if not os.path.exists('imgs'):
    os.mkdir('imgs')

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S').replace(":", "_")
plt.savefig(f'imgs/frequency_plot_{search_content}{time_stamp}.png')

plt.show()