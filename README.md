# getDBLP

## 1 Decribe

表格化dblp搜索结果

## 2 Version
  
- Version 1.0

为了方便查看 https://dblp.org/ 中的论文搜索信息，将查询后的数据进行了一些处理


## 3 Introduction


- 原始搜索结果：(不够直观)

![](https://raw.github.com/yaunsine/getDBLP/master/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20221219210844.png)



- 实现将搜索结果表格化

![](https://raw.github.com/yaunsine/getDBLP/master/Snipaste_2022-12-19_21-06-14.png)



直观显示了所有搜索结果，每个字段代表的含义：

authors:   作者

title：论文标题

venue：发表的刊物（WWW、AAAI等）

type：刊物的类型（期刊、会议等）

year：出版的年份

access：是否开发获取

ee：出版处原文



整理的数据可以方便用于数据分析。
