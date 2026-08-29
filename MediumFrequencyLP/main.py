import random
import function


# (模拟)真实市场价格 | api读取
now_price = round(random.uniform(1, 5), 4)
print("初始市场价格：", now_price)

# 设置固定做市价差 | config设置
spread = 0.05

# 生成初始买卖挂单
price_list = function.price_update(now_price, spread, "initial")
print("初始挂单：", price_list)


# 首次执行挂单更新
trade_price = random.choice(price_list[3:5]) # (模拟)挂单后真实市场成交 | api读取
print("挂单成交价格：", trade_price)

# 后续自动化挂单更新
i = 0
while i < 5:
    new_price_list = function.price_update(trade_price, spread, "update") # 根据成交价格更新挂单
    print("更新后挂单：", new_price_list)
    trade_price = random.choice(new_price_list[3:5])
    print("挂单成交价格：", trade_price)
    print(i+1)
    i = i + 1