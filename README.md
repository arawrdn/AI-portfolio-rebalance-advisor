# AI-Driven Portfolio Rebalance Advisor

This project provides an AI-powered tool to analyze your crypto portfolio and generate optimal rebalancing suggestions. It helps maintain your target allocation, manage risk, and visualize portfolio changes.

## Features

- Analyze multi-token crypto portfolios
- Generate AI-driven rebalancing suggestions
- Optional integration with CoinGecko API for live prices
- Risk and volatility assessment per token
- Visualize portfolio before and after rebalance
- Optional React dashboard

## All-in-One Installation, Usage, Backend, Guide, and Notes

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/ai-portfolio-rebalance-advisor.git
cd ai-portfolio-rebalance-advisor

# 2. Install Python dependencies
pip install pandas numpy scikit-learn matplotlib requests

# 3. Optional: Install frontend dependencies for dashboard
cd dashboard
npm install

# 4. Backend Usage (Python)
python scripts/fetch_prices.py          # Fetch current token prices
python scripts/calculate_rebalance.py   # Compute suggested rebalance
python scripts/visualize_portfolio.py   # Generate plots

# 5. Frontend Dashboard (Optional)
cd dashboard
npm run dev
# Open http://localhost:5173 to view portfolio visualization

# 6. Notes
# - Designed for educational/research purposes, not financial advice
# - Supports multi-token and multi-chain portfolios
# - Data accuracy depends on API sources or offline CSV
# - AI suggestions can be adjusted with target allocation and risk tolerance
