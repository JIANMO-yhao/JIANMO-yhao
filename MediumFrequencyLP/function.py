import math

# 挂单价位设置
# 输入：(参考价格, 价差, 报价模式)
# 输出：[买卖订单挂单价位（从高到低）]
def price_update(reference_price, spread, mode):    # mode == "initial" or "update"
    # 初始价格输入后挂单初始位置
    if mode == 'initial':
        buy1 = math.floor(reference_price / spread) * spread
        buy2 = buy1 - spread
        buy3 = buy1 - 2 * spread
        buy4 = buy1 - 7 * spread
        sell1 = buy1 + 2 * spread
        sell2 = sell1 + spread
        sell3 = sell1 + 2 * spread
        sell4 = sell1 + 7 * spread
        return [
            round(x, 2) 
            for x in [sell4, sell3, sell2, sell1, buy1, buy2, buy3, buy4]
        ]
    
    # 前一笔挂单成交后挂单更新位置
    elif mode == 'update':
        sell4 = reference_price + 8 * spread
        sell3 = reference_price + 3 * spread
        sell2 = reference_price + 2 * spread
        sell1 = reference_price + spread
        buy1 = reference_price - spread
        buy2 = reference_price - 2 * spread
        buy3 = reference_price - 3 * spread
        buy4 = reference_price - 8 * spread
        return [
            round(x, 2) 
            for x in [sell4, sell3, sell2, sell1, buy1, buy2, buy3, buy4]
        ]
    else:
        raise ValueError("mode 必须是 'initial' 或 'update'，请检查输入结果！")
