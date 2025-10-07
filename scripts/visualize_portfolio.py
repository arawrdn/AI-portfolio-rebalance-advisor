import pandas as pd
import matplotlib.pyplot as plt

portfolio = pd.read_csv('../data/portfolio.csv')
rebalance = pd.read_csv('../data/rebalance_suggestions.csv')

# Pie chart before rebalance
plt.figure(figsize=(6,6))
plt.pie(portfolio['amount']*portfolio['price_usd'], labels=portfolio['token'], autopct='%1.1f%%')
plt.title("Portfolio Before Rebalance")
plt.show()

# Pie chart after rebalance
plt.figure(figsize=(6,6))
plt.pie(rebalance['suggested_usd'], labels=rebalance['token'], autopct='%1.1f%%')
plt.title("Portfolio After Rebalance")
plt.show()
