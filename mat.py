import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['simhei']
plt.rcParams['axes.unicode_minus'] = False

data = {'法国': 1, '云南': 1, '安徽': 1, '河南': 4, '江西': 1, '韩国': 1, '北京': 7, '湖北': 1, '海外': 1, '山东': 21, '广东': 10, '陕西': 1, '辽宁': 2, '美国': 9, '上海': 5, '河北': 2, '湖南': 3, '江苏': 8, '黑龙江': 2, '海南': 1, '福建': 2, '浙江': 7, '广西': 1}
cities = data.keys()
values = [x for x in data.values()]
colors = np.random.randn(50)
# num = np.array([13325, 9403, 9227, 8651])
# ratio = np.array([0.75, 0.76, 0.72, 0.75])
# men = num * ratio
# women = num * (1 - ratio)
# x = ['聊天', '支付', '团购\n优惠券', '在线视频']

width = 0.5
idx = np.arange(len(cities))
print(idx)
plt.bar(idx, values, width, color=['b','g','r','c','m','y'])
# plt.bar(idx, men, width, color='red', label='男性用户')
# plt.bar(idx, women, width, bottom=men, color='yellow', label='女性用户')
# plt.xlabel('应用类别')
# plt.ylabel('男女分布')
# plt.xticks((idx + width) , cities, rotation=0)
plt.legend()
plt.show()