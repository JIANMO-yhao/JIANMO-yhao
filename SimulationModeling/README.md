<div align="center">

# Stock Price Simulation

</div>

<!-- &emsp; This is a space. -->
&emsp;&emsp; Considering the dynamics of stock prices in real financial markets, we assume that they exhibit the following three characteristics:

Assumption 1: Annualized returns are relatively stable;

Assumption 2: In the absence of special events, stock prices exhibit continuous random fluctuations;

Assumption 3: Special events can cause instantaneous shocks to stock prices.

Therefore, we use a jump-diffusion process to model the dynamics of the stock price. 
Since the stock price satisfies $S_t>0$ , we define the log-price as:

$$ X_t = \ln S_t $$

We further assume that the log-stock price follows the following jump-diffusion process:

$$ dX_t = \mu_X dt + \sigma dW_t + J_t dN_t $$

Where $W_t$ is a standard Brownian motion, $N_t$ is a Poisson process with intensity $\lambda$ , and $J_t$ represents the size of an individual jump, which follows a double-exponential distribution.

Integrating the above stochastic differential equation gives:

$$ X_t = X_0 + \mu_X t + \sigma W_t + \sum_{i=1}^{N_t}J_i $$

Therefore, the stock price is given by:

$$ S_t = S_0 \exp \left(\mu_X t + \sigma W_t + \sum_{i=1}^{N_t}J_i \right) $$

Then we obtain:

$$
\begin{aligned}
\mathbb{E}[S_t]
&=\mathbb{E} \left[ S_0 e^{\mu_X t} e^{\sigma W_t} e^{\sum_{i=1}^{N_t}J_i}\right]\\
&= S_0 e^{\mu_X t} \mathbb{E} \left[e^{\sigma W_t} e^{\sum_{i=1}^{N_t}J_i}\right] \\
& \Rightarrow S_0 e^{\mu_X t} \mathbb{E}[e^{\sigma W_t}] \mathbb{E}[e^{\sum_{i=1}^{N_t}J_i}] 
\end{aligned}
$$
where the Brownian motion $W_t$, the Poisson process $N_t$, and the jump sizes $\{J_i\}_{i \geq 1}$ are assumed to be mutually independent.

&emsp;&emsp; Firstly, let $Z_t = \sigma W_t$ and $Y_t = e^{Z_t}$. We have:

$$ f_Z(z) = \frac{1}{\sqrt{2 \pi \sigma^2 t}} e^{- \frac{z^2}{2 \sigma^2 t}} $$

We obtain:

$$
\begin{aligned}
\mathbb{E}[Y_t] 
&= \mathbb{E}[e^{Z_t}]\\
&= \int_{- \infty}^{+ \infty} e^z \frac{1}{\sqrt{2 \pi \sigma^2 t}} e^{- \frac{z^2}{2 \sigma^2 t}} dz\\
&= \int_{- \infty}^{+ \infty} \frac{1}{\sqrt{2 \pi \sigma^2 t}} e^{- \frac{(z - \sigma^2 t)^2}{2 \sigma^2 t} + \frac{1}{2} \sigma^2 t} dz\\
&= e^{\frac{1}{2} \sigma^2 t}
\end{aligned}
$$

&emsp;&emsp; Secondly, we assume $N_t=n$, we have:

$$ \sum_{i=1}^{N_t}J_i = J_1 + … + J_n $$

So,

$$ e^{\sum_{i=1}^{N_t}J_i} = e^{J_1 + … + J_n} = e^{J_1}e^{J_2}…e^{J_n} $$

Furthermore, $J_1, J_2, … , J_n$ are independent and identically distributed (i.i.d.), so:

$$ \mathbb{E}[e^{J_1} … e^{J_n}] = (\mathbb{E}[e^J])^n $$

Then,

$$ \mathbb{E}(e^{\sum_{i=1}^{N_t}J_i} \mid N_t = n) = (\mathbb{E}[e^J])^n $$

Since $N_t \sim \operatorname{Poisson}(\lambda t)$, its probability mass function is given by

$$\mathbb{P}(N_t = n) = e^{- \lambda t} \frac{(\lambda t)^n}{n!}$$

So,

$$
\begin{aligned}
\mathbb{E}[e^{\sum_{i=1}^{N_t} J_i}]
&= \sum_{n=0}^{\infty} \mathbb{E} \left[ e^{\sum_{i=1}^{N_t} J_i} \mid N_t = n\right] \mathbb{P}(N_t = n)\\
&= \sum_{n=0}^{\infty} (\mathbb{E}[e^J])^n e^{- \lambda t} \frac{(\lambda t)^n}{n!}\\
&= e^{- \lambda t} \sum_{n=0}^{\infty} \frac{(\lambda t \mathbb{E}[e^J])^n}{n!}
\end{aligned}
$$

With $e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}$, we get:

$$
\begin{aligned}
\mathbb{E}[e^{\sum_{i=1}^{N_t} J_i}]
&= e^{- \lambda t} e^{\lambda t \mathbb{E}[e^J]}\\
&= e^{\lambda t ( \mathbb{E}[e^J] - 1)}
\end{aligned}
$$

Substituting the above stock price process into the expectation condition, and using the moment-generating functions of the Brownian motion and the compound Poisson process, we obtain:

$$
\begin{aligned}
\mathbb{E}[S_t]
&= S_0 e^{\mu_X t} \mathbb{E}[e^{\sigma W_t}] \mathbb{E}[e^{\sum_{i=1}^{N_t}J_i}]\\
&= S_0 \exp \left[ \left( \mu_X + \frac{1}{2}\sigma^2 + \lambda( \mathbb{E}[e^J]-1)\right)t\right] 
\end{aligned}
$$

&emsp;&emsp; At the same time, we require the model to have an annualized expected return of $\mu_S$ , such that:

$$ \frac{ d \mathbb{E}[S_t]}{ \mathbb{E}[S_t]} = \mu_S dt  $$

Comparing this with the target condition:

$$ \mathbb{E}[S_t] = S_0 e^{\mu_S t} $$

We obtain:

$$ \mu_S = \mu_X + \frac{1}{2} \sigma^2 + \lambda (\mathbb{E}[e^J]-1) $$

Then,

$$ \mu_X = \mu_S - \frac{1}{2} \sigma^2 - \lambda (\mathbb{E}[e^J]-1) $$

&emsp;&emsp; Thirdly, 


---
> *"Build from first principles."*
