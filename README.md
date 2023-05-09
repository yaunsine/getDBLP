# dblp-excel-graph
![python-version](https://img.shields.io/badge/python-3.7-red.svg)
![version](https://img.shields.io/badge/version-1.2.0-green.svg)
![lisence](https://img.shields.io/badge/lisence-MIT%20Lisence-blue.svg)


### :green_apple:1 Decribe

表格化dblp搜索结果， 统计图生成， 词云图生成


### dblp介绍

dblp 计算机科学书目提供有关主要计算机科学期刊和会议记录的开放书目信息，dblp 最初于 1993 年在特里尔大学创建
。为了方便查看 
[https://dblp.org/]()
中的论文搜索信息，将查询后的数据进行了一些处理。
- 将搜索结果表格化
- 根据搜索结果生成词云图
- 生成折线图



### :construction_worker:3 Introduction


- 原始搜索结果：(不够直观)

![](https://raw.github.com/yaunsine/getDBLP/master/imgs/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20221219210844.png)



- 实现将搜索结果表格化

![](https://raw.github.com/yaunsine/getDBLP/master/imgs/Snipaste_2022-12-19_21-06-14.png)



### 字段说明

:wrench:直观显示了所有搜索结果，每个字段代表的含义：

|*字段|*描述|
|----|----|
|authors|  作者|
|title|论文标题|
|venue|发表的刊物（WWW、AAAI等）|
|type|刊物的类型（期刊、会议等）|
|year|出版的年份|
|access|是否开发获取|
|ee|出版处原文|


### :package:如何运行？
1. 生成论文列表
```python
python getPaper.py
```

![](https://raw.github.com/yaunsine/getDBLP/master/imgs/Snipaste_2022-12-19_21-06-14.png)


2. 根据搜索结果生成词云图
```python
python cloudword.py
```

![](https://raw.github.com/yaunsine/getDBLP/master/imgs/cloudword.png)

3. 生成折线图
```python
python showDataGraph.py
```

![](https://raw.github.com/yaunsine/getDBLP/master/imgs/frequency_plot.png)


整理的数据可以方便用于数据分析。
