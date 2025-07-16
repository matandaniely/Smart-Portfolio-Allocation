# 📊 Robo-Advisor Portfolio Analyzer

An interactive investment advisory tool built in Python that simulates personalized portfolios based on user preferences and risk profiles. The application combines financial analytics, portfolio optimization, and an intuitive Gradio interface to deliver insights on asset allocation, ESG integration, and investment performance.

---

## 🚀 Features

- **User Questionnaire**: Collects personal and financial details including investment goals, income, net worth, and ESG preference.
  <img width="1470" height="956" alt="User Personal Info" src="https://github.com/user-attachments/assets/a4736a81-1f4d-460e-9030-78cd44e39b29" />

- **Risk Profiling**: Uses behavioral questions to assess user risk appetite and classify into Conservative, Moderate, or Aggressive profiles.
- <img width="1470" height="956" alt="Risk Profile" src="https://github.com/user-attachments/assets/6bd8f913-a518-4c49-bd46-88c05f3b6872" />

- **Portfolio Analyzer**: 
  - Simulates portfolio growth over time based on historical data.
  - Calculates key performance metrics: annualized return, volatility, Sharpe ratio.
  - Generates asset-level insights and correlation heatmaps.
    <img width="1470" height="956" alt="Portfolio Analyzer" src="https://github.com/user-attachments/assets/d7f96b30-a6ff-4996-b141-7b7364f52ae0" />
    <img width="1470" height="956" alt="Asset Level Metrics" src="https://github.com/user-attachments/assets/a813a98e-fed5-4d87-a0ce-6eca47cba65b" />


- **Efficient Frontier Optimization**:
  - Visualizes optimal portfolios based on risk-return trade-offs.
  - Implements constraints for diversification (min 5% per asset, max 5 assets).
  - Compares Sharpe-optimal and minimum-volatility portfolios for ESG and non-ESG universes.
  - <img width="1470" height="956" alt="Efficient Frontier" src="https://github.com/user-attachments/assets/1ad7632f-883b-4dcf-b137-5b0cc0211220" />

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
