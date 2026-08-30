考虑真实市场股票价格变动，我们认为，其具有如下三个特征：

①年化收益相对稳定；

②无特殊情况发生时，股票价格呈现布朗运动状态；

③特殊事件会对股票价格造成冲击；

故此，对股票价格$S_t$ 进行如下建模：
$$dS_t = \mu dt + \sigma dW_t + J_t dN_t$$

其中，$S_t$ 为股票价格，$\mu$ 为预期年化收益，$\sigma$ 为常规波动率，$W_t$ 为随机布朗运动，$J_t$ 为双向指数分布，$N_t$ 为泊松分布。

考虑到$S_t>0$ 并且存在$t=T$ 时，$W_t$，$J_t<0$ ，故取$X_t = ln S_t$ 并：
$$dX_t = \mu dt + \sigma dW_t + J_t dN_t$$
那么，对用户，期望收益为：
$$\frac{d\mathbb{E}[S_t]}{\mathbb{E}[S_t]} = \mu_S dt$$
求解有：
$$\mathbb{E}[S_t] = S_0 e^{\mu_S t}$$
又对真实股票价格有：
$$dX_t = \mu_X dt + \sigma dW_t + J_t dN_t$$
求解有：
$$X_t = X_0 +\mu_X t + \sigma W_t + \sum_{i=1}^{N_t}J_i$$
