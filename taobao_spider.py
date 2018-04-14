import urllib.request
import re
import json
import http.cookiejar
import time

data = []
url1 = 'https://s.taobao.com/search?q=python&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180407&ie=utf8'
headers = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Host": "s.taobao.com"
}
cookies = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookies)
opener = urllib.request.build_opener(handler)
request = urllib.request.Request(url=url1,headers=headers)
response = opener.open(request)
for item in cookies:
    headers['cookies']=item.value
print(headers)
# req = urllib.request.Request(url=url,headers=headers)
# res = urllib.request.urlopen(req)
html = response.read()
# saveFile(html)
html = html.decode('utf-8')
print(html)
# js = r'g_page_config = (.*?)g_srp_loadCss'
# pattern = re.compile(js,re.S)
# content = re.findall(pattern,html)[0].strip()[:-1]
# print(content)
# content = json.loads(content)
# item_list = content['mods']['itemlist']['data']['auctions']
# for item in item_list:
#     temp = {
#         "title": item["title"],
#         "price": item["view_price"],
#         "fee": '否' if item["view_fee"] else '是',
#         "area": item["item_loc"],
#         "sales": item["view_sales"],
#         "name": item["nick"],
#         "isTmall": '是' if item["shopcard"]["isTmall"] else '否',
#         "detail_url": item["detail_url"]
#     }
#     data.append(temp)
# # for item in data:
# #     print(item)
# # data = []
# #首页12条异步加载
# url = 'https://s.taobao.com/api?_ksTS=1523033022993_208&callback=jsonp209&ajax=true&m=customized&stats_click=search_radio_all:1&q=python&s=36&imgfile=&initiative_id=staobaoz_20180407&bcoffset=-1&js=1&ie=utf8&rn=ca67ca59d1ac312ae7ee5f50569d0437'
# request = urllib.request.Request(url=url,headers=headers)
# response = opener.open(request)
# html = response.read()
# html = html.decode('utf-8')
# content = re.findall(r'{.*}',html)[0].strip()
# content = json.loads(content)
# # print(content2)
# item_list = content["API.CustomizedApi"]["itemlist"]["auctions"]
# for item in item_list:
#     temp = {
#         "title": item["title"],
#         "price": item["view_price"],
#         "fee": '否' if item["view_fee"] else '是',
#         "area": item["item_loc"],
#         "sales": item["view_sales"],
#         "name": item["nick"],
#         "isTmall": '是' if item["shopcard"]["isTmall"] else '否',
#         "detail_url": item["detail_url"]
#     }
#     data.append(temp)
# print(len(data))
# # for item in data:
# #     print(item)
#
# # count = 1
# for i in range(1,5):
#     ksts = time.time()
#     _ksTs = '%s_%s'%(str(ksts*1000).split('.')[0],str(ksts*1000).split('.')[1])
#     callback = 'jsonp%s'%(int(str(ksts)[-3:])+1)
#     data_value = 44*i
#     url = 'https://s.taobao.com/search?data-key=s&data-value={}&ajax=true&_' \
#           'ksTS={}&callback={}&q=python&imgfile=&commend=all&ssid=s5-e&search_' \
#           'type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_' \
#           'id=tbindexz_20170306&bcoffset=3&ntoffset=0&p4ppushleft=1%2C48'.format(data_value,_ksTs,callback)
#     request = urllib.request.Request(url=url,headers=headers)
#     # response = request.get(url,cookies=cookies)
#     response = opener.open(request)
#     # cookies = response.cookies
#     # print(response)
#     html = response.read()
#     html = html.decode('utf-8')
#     # print(url)
#     print(html)
#     # print(url)
#     # print(count)
#     # count += 1
#     # 分析
#     content = re.findall(r"{.*}",html)[0]
#     # 格式化json
#     content = json.loads(content)
#     print(content)
#     # 数据列表
#     item_list = content['mods']['itemlist']['data']['auctions']
#     # 提取数据
#     for item in item_list:
#         temp = {
#             "title": item["title"],
#             "price": item["view_price"],
#             "fee": '否' if item["view_fee"] else '是',
#             "area": item["item_loc"],
#             "sales": item["view_sales"],
#             "name": item["nick"],
#             "isTmall": '是' if item["shopcard"]["isTmall"] else '否',
#             "detail_url": item["detail_url"]
#         }
#         data.append(temp)
#     print(len(data))
