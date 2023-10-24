import pandas as pd


# 佳庆指标
def chaikin_oscillator(df, periods_short, periods_long):
    ac = pd.DataFrame()
    val_last = 0

    for date, row in df.iterrows():
        if row.high != row.low:
            val = val_last + ((row.close - row.low) - (row.high - row.close)) / (row.high - row.low) * row.vol
        else:
            val = val_last
        ac.loc[date, 'ac'] = val
        val_last = val

    ema_short = ac.ewm(ignore_na=False, min_periods=0, com=periods_short, adjust=True).mean()
    ema_long = ac.ewm(ignore_na=False, min_periods=0, com=periods_long, adjust=True).mean()

    df.ch_osc = ema_short - ema_long
    return df.ch_osc


# 结合佳庆指标的择时因子
def chaikin_oscillator_timing(df, periods_short, periods_long):
    """
    Chaikin Oscillator上穿0, 且股价高于90天移动平均, side记为 1
    Chaikin Oscillator下穿0, 且股价低于90天移动平均, side记为 -1
    否则side记为 0
    """
    df.ch_osc = chaikin_oscillator(df, periods_short=periods_short, periods_long=periods_long)
    df.SMA_90 = df.close.rolling(90).mean().shift(1)
    df.side = 0
    df.loc[(df.ch_osc.diff(1) > df.ch_osc) & (df.ch_osc > 0) & (df.close > df.SMA_90), 'side'] = 1
    df.loc[(df.ch_osc.diff(1) < df.ch_osc) & (df.ch_osc < 0) & (df.close < df.SMA_90), 'side'] = -1
    return df.side
