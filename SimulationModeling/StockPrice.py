import numpy as np
from dataclasses import dataclass

# 封装"金融模型类"+"仿真模拟类"
@dataclass
class ModelParams:              # 金融模型类
    S0:float                    # 初始股票价格(如 100.00)
    miuS:float                  # 股票年化期望收益率(如 0.12)
    sigma:float                 # 正态分布标准差/年化连续波动率(如 0.15)
    probJplus:float             # 双向指数分布正向跳跃概率(如 0.3)
    miuJ:float                  # 正向跳跃平均幅度/期望值(如 0.05)
    alpha:float                 # 负向跳跃相对倍数(alpha > 1，如 2.5 表示负跳平均幅度为 0.05 * 2.5 = 0.125)
    lamda:float                 # 泊松分布强度/年化跳跃频率(如 12)
@dataclass
class SimulationParams:         # 仿真模拟类
    T:float                     # 时间长度/年(如 1.00)
    N:int                       # 总步数/T
    num_paths:int               # 仿真次数
    seed:int | None = None      # 随机种子

# 参数输入设置
model = ModelParams(            # 金融模型类
    S0=100,
    miuS=0.12,
    sigma=0.15,
    probJplus=0.3,
    miuJ=0.05,
    alpha=1.5,
    lamda=100
)
simulation = SimulationParams(  # 仿真模拟类
    T=1,
    N=365,
    num_paths=1,
    seed=88
)

# 股票价格仿真函数
# 年化期望：d(E[St]) / E[St] = μS dt --> E[St] = S0 * exp(μS * t)
# 股价生成：dXt = μX dt + σ dWt + Jt dNt | Xt = lnSt
# 其中：Wt服从正态分布，Jt服从双向指数分布，Nt服从泊松分布
def stock_price_simulation(model, simulation):
    dt = simulation.T / simulation.N                # 单位步长代表时间/年
    print(model.S0)
    return dt

print(stock_price_simulation(model, simulation))    # 仿真测试
