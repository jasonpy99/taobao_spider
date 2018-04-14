import requests
import re
import json
import time
#数据
data = []

url = 'https://s.taobao.com/search?q=python&imgfile=&commend=all&ssid=s5-e&search_' \
      'type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'
#发送http请求
response = requests.get(url)
#html源码
html = response.text
#分析
content = re.findall(r'g_page_config = (.*?)g_srp_loadCss',html,re.S)[0].strip()[:-1]
#格式化json
content = json.loads(content)
#数据列表
item_list = content['mods']['itemlist']['data']['auctions']
#提取数据
for item in item_list:
    temp = {
        "title":item["title"],
        "price":item["view_price"],
        "fee":'否' if item["view_fee"] else '是',
        "area":item["item_loc"],
        "sales":item["view_sales"],
        "name":item["nick"],
        "isTmall":'是' if item["shopcard"]["isTmall"] else '否',
        "detail_url":item["detail_url"]
    }
    data.append(temp)
for item in data:
    print(item)
data = []
#cookie保持
cookies = response.cookies
# print(cookies)
#首页12条异步加载
url2 = 'https://s.taobao.com/api?_ksTS=1523032441741_226&callback=jsonp227&ajax=true&m=customized&stats_click=search_radio_all:1&q=python&s=36&imgfile=&initiative_id=staobaoz_20180407&bcoffset=-1&js=1&ie=utf8&rn=30643ea272f0f5cfd66c06df501b0ee9'
response2 = requests.get(url2,cookies=cookies)
html2 = response2.text
content2 = re.findall(r'{.*}',html2)[0].strip()
print(content2)
content2 = json.loads(content2)
item_list2 = content2["API.CustomizedApi"]["itemlist"]["auctions"]
for item in item_list2:
    temp = {
        "title": item["title"],
        "price": item["view_price"],
        "fee": '否' if item["view_fee"] else '是',
        "area": item["item_loc"],
        "sales": item["view_sales"],
        "name": item["nick"],
        "isTmall": '是' if item["shopcard"]["isTmall"] else '否',
        "detail_url": item["detail_url"]
    }
    data.append(temp)
for item in data:
    print(item)
# print(len(data))
# print(content)
# print(html2)
# print(len(data))
# cookies = response.cookies
count = 1
for i in range(1,10):
    ksts = time.time()
    _ksTs = '%s_%s'%(str(ksts*1000).split('.')[0],str(ksts*1000).split('.')[1])
    callback = 'jsonp%s'%(int(str(ksts)[-3:])+1)
    data_value = 44*i
    url = 'https://s.taobao.com/search?data-key=s&data-value={}&ajax=true&_' \
          'ksTS={}&callback={}&q=python&imgfile=&commend=all&ssid=s5-e&search_' \
          'type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_' \
          'id=tbindexz_20170306&bcoffset=3&ntoffset=0&p4ppushleft=1%2C48'.format(data_value,_ksTs,callback)
    response = requests.get(url,cookies=cookies)
    cookies = response.cookies
    print(response)
    html = response.text
    print(url)
    print(html)
    print(url)
    print(count)
    count += 1
    # 分析
    content = re.findall(r"{.*}",html)[0]
    # 格式化json
    content = json.loads(content)
    print(content)
    # 数据列表
    item_list = content['mods']['itemlist']['data']['auctions']
    # 提取数据
    for item in item_list:
        temp = {
            "title": item["title"],
            "price": item["view_price"],
            "fee": '否' if item["view_fee"] else '是',
            "area": item["item_loc"],
            "sales": item["view_sales"],
            "name": item["nick"],
            "isTmall": '是' if item["shopcard"]["isTmall"] else '否',
            "detail_url": item["detail_url"]
        }
        data.append(temp)
print(len(data))