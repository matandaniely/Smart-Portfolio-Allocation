# config.py

DARK_MODE_STYLE = 'dark_background'

# Define assets and their tickers
assets = {
    'Bonds US: Treasury Yield 20 Years': '^TYX',
    'Bonds US - High Yield Corporate': 'HYG',
    'Bonds Emerging Markets': 'EMB',
    'Bonds Inflation-Linked: iShares TIPS ETF': 'TIP',
    'Equity - US: SP500': 'SPY',
    'Equity - US: Technology Sector': 'XLK',
    'Equity - World: Emerging Markets': 'IEMG',
    'Equity - World: Developed Markets': 'VEA',
    'Real Estate - Global REIT': 'REET',
    'Real Estate - US REIT ETF': 'VNQ',
    'Real Estate - High Dividend REIT': 'KBWY',
    'Commodities - Gold': 'GLD',  # Changed from GC=F to GLD (ETF proxy)
    'Commodities - Oil': 'USO',   # Changed from CL=F to USO (ETF proxy)
    'Commodities - Natural Gas': 'UNG',
    'Cryptocurrency - Bitcoin': 'BTC-USD',
    'Cryptocurrency - Ethereum': 'ETH-USD',
    'ESG - iShares ESG Aware MSCI USA ETF': 'ESGU',
    'ESG - Vanguard ESG International Stock ETF': 'VSGX',
    'Clean Energy - iShares Global Clean Energy ETF': 'ICLN',
    'Green Bonds - VanEck Green Bond ETF': 'GRNB',
}


# Portfolio allocations (same as yours)
portfolio_allocations = {
    "Yes": {
        "Conservative": {
            "Bonds US: Treasury Yield 20 Years": 0.25,
            "Bonds US - High Yield Corporate": 0.20,
            "Bonds Emerging Markets": 0.10,
            "Bonds Inflation-Linked: iShares TIPS ETF": 0.15,
            "Commodities - Gold": 0.10,
            "Green Bonds - VanEck Green Bond ETF": 0.20,
        },
        "Moderate": {
            "Equity - US: SP500": 0.15,
            "Equity - US: Technology Sector": 0.15,
            "Equity - World: Developed Markets": 0.10,
            "Bonds US: Treasury Yield 20 Years": 0.10,
            "Bonds US - High Yield Corporate": 0.10,
            "Real Estate - Global REIT": 0.10,
            "Commodities - Gold": 0.10,
            "ESG - iShares ESG Aware MSCI USA ETF": 0.15,
            "Clean Energy - iShares Global Clean Energy ETF": 0.15,
        },
        "Aggressive": {
            "Equity - US: SP500": 0.10,
            "Equity - US: Technology Sector": 0.10,
            "Equity - World: Emerging Markets": 0.10,
            "Real Estate - Global REIT": 0.05,
            "Cryptocurrency - Bitcoin": 0.15,
            "Cryptocurrency - Ethereum": 0.05,
            "Commodities - Gold": 0.05,
            "Commodities - Oil": 0.05,
            "ESG - Vanguard ESG International Stock ETF": 0.10,
            "Clean Energy - iShares Global Clean Energy ETF": 0.15,
        },
    },
    "No": {
        "Conservative": {
            "Bonds US: Treasury Yield 20 Years": 0.30,
            "Bonds US - High Yield Corporate": 0.25,
            "Bonds Emerging Markets": 0.15,
            "Bonds Inflation-Linked: iShares TIPS ETF": 0.20,
            "Commodities - Gold": 0.10,
        },
        "Moderate": {
            "Equity - US: SP500": 0.20,
            "Equity - US: Technology Sector": 0.20,
            "Equity - World: Developed Markets": 0.15,
            "Bonds US: Treasury Yield 20 Years": 0.15,
            "Bonds US - High Yield Corporate": 0.10,
            "Real Estate - Global REIT": 0.10,
            "Commodities - Gold": 0.10,
        },
        "Aggressive": {
            "Equity - US: SP500": 0.15,
            "Equity - US: Technology Sector": 0.15,
            "Equity - World: Emerging Markets": 0.15,
            "Real Estate - Global REIT": 0.10,
            "Cryptocurrency - Bitcoin": 0.20,
            "Cryptocurrency - Ethereum": 0.10,
            "Commodities - Gold": 0.10,
            "Commodities - Oil": 0.05,
        }
    }
}