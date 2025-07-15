import yfinance as yf
import pandas as pd

def fetch_asset_data(assets, start='2019-01-01', end='2024-11-30', save=False):
    prices = pd.DataFrame()
    failed_assets = []

    for name, symbol in assets.items():
        try:
            data = yf.download(symbol, start=start, end=end)
            prices[name] = data['Adj Close']
        except Exception as e:
            failed_assets.append(name)
    
    prices.dropna(inplace=True)
    returns = prices.pct_change().dropna()

    if save:
        prices.to_csv("assets/asset_data.csv")
        returns.to_csv("assets/asset_returns.csv")

    return prices, returns
