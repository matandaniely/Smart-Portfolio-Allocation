# Robo-Advisor Portfolio Analyzer

An interactive investment advisory tool built in Python that simulates personalized portfolios based on user preferences and risk profiles. The application combines financial analytics, portfolio optimization, and an intuitive Gradio interface to deliver insights on asset allocation, ESG integration, and investment performance.

---

## Features

- **User Questionnaire**: Collects personal and financial details including investment goals, income, net worth, and ESG preference.       This part is aimed at simulating a registration phase. It does not effect other stages in the process and does not save the information.     
<img width="1021" height="681" alt="User Personal Info" src="https://github.com/user-attachments/assets/dd9f46cb-3c4e-46f6-9466-6473e05afa9f" />


- **Risk Profiling**: Uses behavioral questions to assess user risk appetite and classify into Conservative, Moderate, or Aggressive profiles.       This questionnaire allows the user to understand what type of an investor they are from three categories:        
  - Conservative (a profile that would prefer safety over gains, the future result of the recommended portfolio would be a low volatilty combination of allocated assets and lower returns).       
  - Moderate (a portfolio that is more balaced, allocating more investments towards riskier assets that promise higher yields).        
  - Aggressive ( a profile that would allocate more investments towards riskier assets, but that have to potential to yield higher returns).      
<img width="1021" height="669" alt="Risk Profile" src="https://github.com/user-attachments/assets/ed18f1a6-c7b7-4f4d-a378-de9f9c5716ab" />


- **Portfolio Analyzer**: This part simulates an easy product for advisors, based on the risk level of the profile (and predefined weights for each asset based on the profile and ESG preference) the customer will recieve metrics of volatilty and sharpe ratio that can help them see what are the expected returns for their investment based on historical data.      

  - Simulates portfolio growth over time based on historical data.    
  - Calculates key performance metrics: annualized return, volatility, Sharpe ratio.    
  - Generates asset-level insights and correlation heatmaps.
  - The suggested portfolio considers all aspects above to generate a portfolio based on the pre-defined weights that a risk profile has.      
<img width="1008" height="664" alt="Portfolio Analyzer" src="https://github.com/user-attachments/assets/4ef37f02-fa5e-4bca-8ee8-f6862212394f" />

Asset Level Metrics:    An allocation distribution table that the customer can see how much they invest and in which type of asset. 
<img width="718" height="620" alt="Asset Level Metriccs" src="https://github.com/user-attachments/assets/d4221c99-a6e1-46d1-bdae-9856eb9f473f" />


- **Efficient Frontier Optimization**:    
This is an advanced tool that constructs an optimized investment portfolio based on a set of given assets. It simulates thousands of possible asset weight combinations (e.g., 5,000 simulations) to generate a graph plotting Expected Return against Volatility. Each point on the graph represents a potential portfolio configuration.     

The key feature of this tool is the efficient frontier—a curve that connects the portfolios offering the highest expected return for a given level of risk (volatility). This frontier helps investors identify optimal portfolios that balance risk and return effectively. By selecting a point on this curve, investors can make more informed decisions about how to allocate their capital across different asset types.       
  - Visualizes optimal portfolios based on risk-return trade-offs.    
  - Implements constraints for diversification (min 5% per asset, max 5 assets). I created this restriction as sometimes it would allocate more than 90% to one type of an asset and 0.01% to another.      
  - Compares Sharpe-optimal and minimum-volatility portfolios for ESG and non-ESG universes.    
<img width="1067" height="669" alt="Efficient Frontier" src="https://github.com/user-attachments/assets/64f53bef-5f74-497c-9cbe-e152fb4d6954" />


---

## Skills Demonstrated

- Financial Analytics & Portfolio Theory (CAPM, Sharpe Ratio, Volatility)     
- Python Libraries: `pandas`, `numpy`, `matplotlib`, `scipy.optimize`, `yfinance`, `seaborn`     
- UI/UX with `gradio` for interactive, tabbed user flows     
- Data Preprocessing, Time Series Returns, and Covariance Estimation    
- Sequential Least Squares Programming (SLSQP) - Optimization under Constraints. SLSQP is often used to optimize portfolio weights subject to constraints   

---

## Project Structure

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
