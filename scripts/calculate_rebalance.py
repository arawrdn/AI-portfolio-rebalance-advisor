import pandas as pd

# Load portfolio and prices
portfolio = pd.read_csv('../data/portfolio.csv')  # columns: token, amount, target_pct
prices = pd.read_csv('../data/prices.csv')        # columns: token, price_usd

portfolio = portfolio.merge(prices, on='token')
portfolio['value_usd'] = portfolio['amount'] * portfolio['price_usd']

# Calculate total portfolio value
total_value = portfolio['value_usd'].sum()

# Calculate current allocation %
portfolio['current_pct'] = portfolio['value_usd'] / total_value * 100

# Calculate suggested rebalance
portfolio['suggested_usd'] = total_value * (portfolio['target_pct'] / 100)
portfolio['delta_usd'] = portfolio['suggested_usd'] - portfolio['value_usd']
portfolio['action'] = portfolio['delta_usd'].apply(lambda x: 'Buy' if x > 0 else 'Sell')

portfolio.to_csv('../data/rebalance_suggestions.csv', index=False)
print("Rebalance suggestions saved to data/rebalance_suggestions.csv")
