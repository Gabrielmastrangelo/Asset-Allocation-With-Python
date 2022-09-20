# Passive Investing

This repository was initially created to share my project for my course in Business Computing.
I wrote an article talking briefly about passive investing and **asset allocation**, 
In the end, I made a historical simulation using **Python**. Now, I am developing this repository to show some
python applications for **asset allocation** and **finance**.

The article content:
- The most important topics that affect returns,
- The efficient market hypothesis,
- Passive investing methodology for individual investors,

[My Linkedin webpage](https://www.linkedin.com/in/gabriel-canuto/)

***OBS***: This repository is heavily based in the Courses of [Assets Management w/ Python from EDHEC](https://www.coursera.org/specializations/investment-management-python-machine-learning)

### 1 - Hello World Portfolio
Here, just to initiate the topic of asset allocation and python for financial applications, we developed a portfolio with no rebalance and no changes.
It is noticeable, that as the equity share of the portfolio outperforms the others classes, it becomes more volatile and less diversified. 
But we will analyze it deeper when we use python for computing portfolio metrics. [Code](1-BasicPortfolio/1-basicPortfolio.ipynb)

![alt text](https://github.com/Gabrielmastrangelo/BCPT-123_Word_Power_Project/blob/main/Plot.png)

### 2 - Fixed Frequency and Weights Rebalancing 
It was introduced a portfolio with the same assets classes and weights as the last one, but this time we had rebalanced the portfolio for fixed weights in a fixed interval of time. It performed worst than the last portfolio in absolute terms (compounded return), but it was more diversified and probably much less volatile. Again, we will compare it better when we introduce the metrics computation for assets. [Code](https://github.com/Gabrielmastrangelo/Asset-Allocation-With-Python/blob/main/2-TimingRebalancing/RebalancingByFrequency.ipynb)

![alt text](https://github.com/Gabrielmastrangelo/Asset-Allocation-With-Python/blob/main/02-TimingRebalancing/Plot.png)

### 3 - Computing Portfolio Metrics
Python applications for calculating annualized return and volatility. This was just the beginning, there is a lot to show when talking about portfolio metrics. And python is a really useful tool for that. [Code](https://github.com/Gabrielmastrangelo/Quantitative-Finance-with-Python/blob/main/3-PortfolioMetrics/3%20-%20portfolioMetrics.ipynb)

![alt text](https://github.com/Gabrielmastrangelo/Quantitative-Finance-with-Python/blob/main/03-PortfolioMetrics/Plot.png)

### 4 - Computing the Historical Drawdown for an Asset or Portfolio
Python application for calculating and plotting the historical drawdown for the SPY index, reflected by the IVV ETF. We can use the same proccedure to calculate the drawdown for any asset or portfolio.

![alt text](https://github.com/Gabrielmastrangelo/Quantitative-Finance-with-Python/blob/main/04-MaxDrawdown/Plot.png)

### 5 - Computing Downside Risk Metrics
We use python to calculate the SemiDeviation, Historic VaR, Historic CVar, Parametric VaR and Cornish-Fisher Parametric VaR.

![alt text](https://github.com/Gabrielmastrangelo/Quantitative-Finance-with-Python/blob/main/05-Downside_RiskMeasures/Plot.png)
