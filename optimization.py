import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from itertools import combinations

def efficient_frontier_plot(esg_option):
    df_return = pd.read_csv("assets/asset_returns.csv", index_col=0, parse_dates=True).dropna()

    if esg_option == "ESG":
        selected_assets = [
            "Green Bonds - VanEck Green Bond ETF",
            "ESG - iShares ESG Aware MSCI USA ETF",
            "Clean Energy - iShares Global Clean Energy ETF",
            "ESG - Vanguard ESG International Stock ETF",
            "Equity - US: SP500",
            "Equity - US: Technology Sector",
            "Bonds US - High Yield Corporate",
            "Bonds US: Treasury Yield 20 Years",
            "Commodities - Gold",
            "Real Estate - Global REIT"
        ]
    else:
        selected_assets = [
            "Equity - US: SP500",
            "Equity - US: Technology Sector",
            "Equity - World: Emerging Markets",
            "Equity - World: Developed Markets",
            "Cryptocurrency - Bitcoin",
            "Cryptocurrency - Ethereum",
            "Bonds US - High Yield Corporate",
            "Bonds US: Treasury Yield 20 Years",
            "Bonds Inflation-Linked: iShares TIPS ETF",
            "Commodities - Gold",
            "Commodities - Oil",
            "Real Estate - Global REIT"
        ]

    returns = df_return[selected_assets]
    mean_returns = returns.mean() * 252
    cov_matrix = returns.cov() * 252
    risk_free_rate = 0.02

    def portfolio_performance(weights):
        ret = np.dot(weights, mean_returns)
        vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        return ret, vol

    def negative_sharpe_ratio(weights):
        ret, vol = portfolio_performance(weights)
        return -(ret - risk_free_rate) / vol

    def minimize_volatility(weights):
        return portfolio_performance(weights)[1]

    num_assets = len(selected_assets)
    bounds = tuple((0, 1) for _ in range(num_assets))
    constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
    initial_weights = num_assets * [1. / num_assets]

    # opt_sharpe = minimize(negative_sharpe_ratio, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)
    # opt_min_vol = minimize(minimize_volatility, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)

    best_sharpe = -np.inf
    best_vol = np.inf
    best_weights_sharpe = None
    best_weights_vol = None
    best_assets_sharpe = None
    best_assets_vol = None

    min_weight = 0.05  # Minimum 5%
    asset_combos = list(combinations(selected_assets, 5))

    for subset in asset_combos:
        sub_returns = returns[list(subset)]
        sub_mean = sub_returns.mean() * 252
        sub_cov = sub_returns.cov() * 252
        n = len(subset)

        def port_perf(w):
            r = np.dot(w, sub_mean)
            v = np.sqrt(np.dot(w.T, np.dot(sub_cov, w)))
            return r, v

        def neg_sharpe(w):
            r, v = port_perf(w)
            return -(r - risk_free_rate) / v

        def min_vol(w):
            return port_perf(w)[1]

        bounds = [(min_weight, 1) for _ in range(n)]
        constraint = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}
        init = np.array([1/n] * n)

        try:
            res_sharpe = minimize(neg_sharpe, init, method='SLSQP', bounds=bounds, constraints=constraint)
            res_vol = minimize(min_vol, init, method='SLSQP', bounds=bounds, constraints=constraint)

            if res_sharpe.success and -res_sharpe.fun > best_sharpe:
                best_sharpe = -res_sharpe.fun
                best_weights_sharpe = res_sharpe.x
                best_assets_sharpe = subset

            if res_vol.success and res_vol.fun < best_vol:
                best_vol = res_vol.fun
                best_weights_vol = res_vol.x
                best_assets_vol = subset
        except:
            continue


    n_portfolios = 5000
    results = np.zeros((3, n_portfolios))
    for i in range(n_portfolios):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)
        r, v = portfolio_performance(weights)
        results[0, i] = v
        results[1, i] = r
        results[2, i] = (r - risk_free_rate) / v

    # sharpe_return, sharpe_volatility = portfolio_performance(opt_sharpe.x)
    # min_return, min_volatility = portfolio_performance(opt_min_vol.x)

    # fig, ax = plt.subplots(figsize=(12, 8))
    # sc = ax.scatter(results[0, :], results[1, :], c=results[2, :], cmap='coolwarm', alpha=0.5)
    # ax.scatter(min_volatility, min_return, marker='*', color='r', s=300, label='Min Volatility')
    # ax.scatter(sharpe_volatility, sharpe_return, marker='*', color='g', s=300, label='Max Sharpe Ratio')
    # ax.set_title(f'Efficient Frontier - {esg_option} Portfolio')
    # ax.set_xlabel('Expected Volatility')
    # ax.set_ylabel('Expected Return')
    # ax.legend()
    # ax.grid(True)
    # fig.colorbar(sc, label='Sharpe Ratio')
    # plt.tight_layout()

    # weights_df = pd.DataFrame({
    #     "Min Volatility Portfolio": opt_min_vol.x,
    #     "Max Sharpe Ratio Portfolio": opt_sharpe.x
    # }, index=returns.columns).applymap(lambda x: f"{x * 100:.2f}%")

    # return_df = pd.DataFrame({
    #     "Portfolio": ["Min Volatility", "Max Sharpe Ratio"],
    #     "Expected Annual Return (%)": [f"{min_return * 100:.2f}%", f"{sharpe_return * 100:.2f}%"]
    # })

    # return fig, weights_df.T.reset_index(), return_df

    # Recalculate with selected weights
    ret_s, vol_s = np.dot(best_weights_sharpe, returns[list(best_assets_sharpe)].mean() * 252), np.sqrt(np.dot(best_weights_sharpe.T, np.dot(returns[list(best_assets_sharpe)].cov() * 252, best_weights_sharpe)))
    ret_v, vol_v = np.dot(best_weights_vol, returns[list(best_assets_vol)].mean() * 252), np.sqrt(np.dot(best_weights_vol.T, np.dot(returns[list(best_assets_vol)].cov() * 252, best_weights_vol)))

    # Plot
    fig, ax = plt.subplots(figsize=(12, 8))
    sc = ax.scatter(results[0, :], results[1, :], c=results[2, :], cmap='coolwarm', alpha=0.5)
    ax.scatter(vol_v, ret_v, marker='*', color='r', s=300, label='Min Volatility')
    ax.scatter(vol_s, ret_s, marker='*', color='g', s=300, label='Max Sharpe Ratio')
    ax.set_title(f'Efficient Frontier - {esg_option} Portfolio (5 Assets Only)')
    ax.set_xlabel('Expected Volatility')
    ax.set_ylabel('Expected Return')
    ax.legend()
    ax.grid(True)
    fig.colorbar(sc, label='Sharpe Ratio')
    plt.tight_layout()

    # Format weights
    weights_df = pd.DataFrame({
        "Min Volatility Portfolio": pd.Series(best_weights_vol, index=best_assets_vol),
        "Max Sharpe Ratio Portfolio": pd.Series(best_weights_sharpe, index=best_assets_sharpe)
    }).applymap(lambda x: f"{x * 100:.2f}%")

    return_df = pd.DataFrame({
        "Portfolio": ["Min Volatility", "Max Sharpe Ratio"],
        "Expected Annual Return (%)": [f"{ret_v * 100:.2f}%", f"{ret_s * 100:.2f}%"]
    })

    return fig, weights_df.T.reset_index(), return_df

