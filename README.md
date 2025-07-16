# 📊 Robo-Advisor Portfolio Analyzer

An interactive investment advisory tool built in Python that simulates personalized portfolios based on user preferences and risk profiles. The application combines financial analytics, portfolio optimization, and an intuitive Gradio interface to deliver insights on asset allocation, ESG integration, and investment performance.

---

## 🚀 Features

- **User Questionnaire**: Collects personal and financial details including investment goals, income, net worth, and ESG preference.
<img width="1021" height="681" alt="User Personal Info" src="https://github.com/user-attachments/assets/dd9f46cb-3c4e-46f6-9466-6473e05afa9f" />


- **Risk Profiling**: Uses behavioral questions to assess user risk appetite and classify into Conservative, Moderate, or Aggressive profiles.
<img width="1021" height="669" alt="Risk Profile" src="https://github.com/user-attachments/assets/ed18f1a6-c7b7-4f4d-a378-de9f9c5716ab" />


- **Portfolio Analyzer**: 
  - Simulates portfolio growth over time based on historical data.
  - Calculates key performance metrics: annualized return, volatility, Sharpe ratio.
  - Generates asset-level insights and correlation heatmaps.
<img width="1008" height="664" alt="Portfolio Analyzer" src="https://github.com/user-attachments/assets/4ef37f02-fa5e-4bca-8ee8-f6862212394f" />

Asset Level Metrics:
<img width="718" height="620" alt="Asset Level Metriccs" src="https://github.com/user-attachments/assets/d4221c99-a6e1-46d1-bdae-9856eb9f473f" />


- **Efficient Frontier Optimization**:
  - Visualizes optimal portfolios based on risk-return trade-offs.
  - Implements constraints for diversification (min 5% per asset, max 5 assets).
  - Compares Sharpe-optimal and minimum-volatility portfolios for ESG and non-ESG universes.
<img width="1067" height="669" alt="Efficient Frontier" src="https://github.com/user-attachments/assets/64f53bef-5f74-497c-9cbe-e152fb4d6954" />


---

## 🧠 Skills Demonstrated

- Financial Analytics & Portfolio Theory (CAPM, Sharpe Ratio, Volatility)
- Python Libraries: `pandas`, `numpy`, `matplotlib`, `scipy.optimize`, `yfinance`, `seaborn`
- UI/UX with `gradio` for interactive, tabbed user flows
- Data Preprocessing, Time Series Returns, and Covariance Estimation
- Optimization under Constraints (SLSQP)

---

## 🗂️ Project Structure

robo-advisor/
├── app.py                 # Main Gradio app logic and layout
├── config.py              # Asset definitions and portfolio weight mappings
├── data_loader.py         # Fetches historical asset price data via yfinance
├── analysis.py            # Portfolio construction and analytics
├── optimization.py        # Efficient Frontier and constrained optimization
├── questionnaire.py       # User and risk profile logic
├── utils.py               # Helper functions (e.g., geometric returns)
├── assets/
│ └── asset_returns.csv    # Preprocessed historical returns
