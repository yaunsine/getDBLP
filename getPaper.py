import requests
import json
import pandas as pd
from urllib.parse import quote
import sys
search_content = "Object detection"         # 输入搜索的内容
search_contents = quote(search_content)
papar_count = 1000      # 输入获取论文的数量
url = "https://dblp.org/search/publ/api?q="+search_contents+"&h="+str(papar_count)+"&format=json"

proxies = {"http": "222.175.22.197:9091"}       # 运行不了改一下代理IP
content = requests.get(url, proxies=proxies).text
content_json = json.loads(content)
if int(content_json['result']['hits']['@total']) <= 0:
    raise Exception('请求无数据')
    # sys.exit(0)
article_ls = content_json['result']['hits']['hit']

# if len(content_json['result']['hits']['hit'])
cols_name = article_ls[0].keys()

data_dict = dict()
ls = [[] for _ in cols_name]

for x in article_ls:
    for i, v in enumerate(x.keys()):
        ls[i].append(x[v])
for i, x in enumerate(cols_name):
    data_dict[x] = ls[i]
    if i == 2:
        auth_ls = []
        lss = [[] for _ in range(9)]
        # lens = len(ls[i][0].keys())
        for j, v1 in enumerate(ls[i]):
            # if lens != len(v1.keys()):
            #     continue
            try:
                lss[0].append(",".join([x['text'] for x in v1['authors']['author']])) if 'authors' in v1 else lss[0].append(None)
                lss[1].append(v1['title']) if 'title' in v1 else lss[1].append(None)
                lss[2].append(v1['venue']) if 'venue' in v1 else lss[2].append(None)
                lss[3].append(v1['type']) if 'type' in v1 else lss[3].append(None)
                lss[4].append(v1['year']) if 'year' in v1 else lss[4].append(None)
                lss[5].append(v1['access']) if 'access' in v1 else lss[5].append(None)
                lss[6].append(v1['key']) if 'key' in v1 else lss[6].append(None)
                lss[7].append(v1['url']) if 'url' in v1 else lss[7].append(None)
                lss[8].append(v1['ee']) if 'ee' in v1 else lss[8].append(None)
            except Exception as e:
                print(v1)
                print(e)
            # dict_keys(['authors', 'title', 'venue', 'pages', 'year', 'type', 'access', 'key', 'doi', 'ee', 'url'])
            # for k, v2 in enumerate(v1.keys()):
            #     # auth = author['authors']['author'][0]['text']
            #     # auth_ls.append(auth)
            #     try:
            #         lss[k].append(v1[v2])
            #     except:
            #         print(k)
        din = ['authors', 'title', 'venue', 'type', 'year', 'access', 'key', 'url', 'ee']
        for i, x in enumerate(din):
            data_dict[x] = lss[i]


del data_dict['info']
del data_dict['@id']
del data_dict['url']
del data_dict['@score']
df = pd.DataFrame(data=data_dict)
search_content = search_content.capitalize().replace(" ", "")
df.index = df.index + 1
df.to_csv(search_content+".csv")
pass