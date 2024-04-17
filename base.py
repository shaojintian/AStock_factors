import yfinance as yf
import pandas as pd

# 获取QQQ的历史数据，时间范围为最近180天
ticker = 'QQQ'
start_date = pd.Timestamp.now() - pd.DateOffset(days=180)
end_date = pd.Timestamp.now()
data = yf.download(ticker, start=start_date, end=end_date)

# 计算收益率
data['Returns'] = data['Adj Close'].pct_change()

data.head()

# 计算最近20日收益率的均值和标准差
last_20_returns = data['Returns'].tail(20)
mean_return = last_20_returns.mean()
std_dev_return = last_20_returns.std()

print(f'最近20日收益率的均值为: {mean_return:.4f}')
print(f'最近20日收益率的标准差为: {std_dev_return:.4f}')
