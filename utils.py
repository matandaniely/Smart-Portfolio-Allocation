def ann_geomean(df):
    df = df.dropna()
    years = (df.index[-1] - df.index[0]).days / 365.25
    return ((df + 1).prod()) ** (1 / years) - 1
