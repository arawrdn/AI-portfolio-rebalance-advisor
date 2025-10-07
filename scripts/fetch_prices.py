```python
import requests
import pandas as pd

# Example tokens and target allocations
tokens = ['bitcoin', 'ethereum', 'solana']
portfolio_file = '../data/portfolio.csv'

# Fetch current prices from CoinGecko
prices = {}
for token in tokens:
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={token}&vs_currencies=usd"
    data = requests.get(url).json()
    prices[token] = data[token]['usd']

# Save current prices
df_prices = pd.DataFrame(list(prices.items()), columns=['token', 'price_usd'])
df_prices.to_csv('../data/prices.csv', index=False)
print("Current token prices saved to data/prices.csv")
