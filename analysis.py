import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_weighted_portfolio(risk_profile, esg_pref, df_return, portfolio_allocations):
    weights_dict = portfolio_allocations[esg_pref][risk_profile]
    tickers = list(weights_dict.keys())
    weights = list(weights_dict.values())

    returns = df_return[tickers].copy().clip(lower=-1, upper=1).fillna(0)
    return returns, tickers, np.array(weights)

def analyze_portfolio(risk_profile, esg_pref, df_return, portfolio_allocations):
    portfolio, tickers, weights = get_weighted_portfolio(risk_profile, esg_pref, df_return, portfolio_allocations)

    weighted_returns = portfolio.mul(weights, axis=1).sum(axis=1)
    cumulative = (1 + weighted_returns).cumprod()

    fig1, ax1 = plt.subplots(figsize=(10, 5))
    cumulative.plot(ax=ax1)
    ax1.set_title(f"Cumulative Portfolio Growth - {risk_profile} | ESG: {esg_pref}")
    ax1.set_ylabel("Growth of $1")
    ax1.set_xlabel("Date")
    ax1.grid(True)
    plt.tight_layout()

    years = (portfolio.index[-1] - portfolio.index[0]).days / 365.25
    ann_returns = ((portfolio + 1).prod()) ** (1 / years) - 1

    cov_matrix = portfolio.cov() * 252
    portfolio_return = np.dot(ann_returns, weights)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    sharpe_ratio = (portfolio_return - 0.02) / portfolio_volatility

    asset_metrics = pd.DataFrame({
        "Annual Return": ann_returns,
        "Weight": weights,
        "Contribution to Return": ann_returns * weights
    }).round(3).reset_index(names="Asset")

    summary = pd.DataFrame({
        "Portfolio Return": [portfolio_return],
        "Portfolio Volatility": [portfolio_volatility],
        "Sharpe Ratio": [sharpe_ratio]
    }).round(3)

    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.heatmap(portfolio.corr(), cmap='vlag', vmin=-1, vmax=1, annot=True, ax=ax2)
    ax2.set_title("Asset Correlation Heatmap")
    plt.tight_layout()

    return fig1, fig2, asset_metrics, summary
