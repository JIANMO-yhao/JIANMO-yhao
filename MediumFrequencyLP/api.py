import random
import math

# 模拟当前价格生成函数
# 输入：价格变动次数(twice)
# 输出：价格变动列表[price_list]
def price_list(twice):
    i = 10
    price_list = []
    while i < 10 + twice:
        now_price = round(math.log(i) + random.choice([-1, 1]) * random.uniform(0, 0.05), 4)
        price_list.append(now_price)
        i = i + 1
    return price_list
# print(price_list(10))     # 测试函数运行是否顺畅

# 配置基本初始状态
money = 100                 # 初始本金余额
stocks = 10                 # 初始库存余额
order_size = 1              # 每笔挂单数目
spread = 0.05               # 每笔挂单价差
