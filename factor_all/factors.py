import pandas as pd
import numpy as np


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


# DMI因子
def DMI(df, window1, window2):
    # tr = max(今日最高价与最低价的价差, 今日最高价与昨日收盘价价差绝对值, 今日最低价与昨日收盘价价差绝对值)
    tr = pd.Series(
        np.vstack([df.high - df.low, (df.high - df.close.shift(1)).abs(), (df.low - df.close.shift(1)).abs()]).max(
            axis=0), index=df.index)

    # tr的window1日之和
    trz = tr.rolling(window1).sum()

    _df = df.copy()
    # 今日最高价高于昨日最高价的部分, 记为hd
    _df['hd'] = _df.high - _df.high.shift(1)
    # 今日最低价低于昨日最低价的部分, 记为ld
    _df['ld'] = _df.low.shift(1) - _df.low
    # hd>0 且 hd>ld, 则mp=hd, 否则为0
    _df['mp'] = _df.apply(lambda x: x.hd if x.hd > 0 and x.hd > x.ld else 0, axis=1)
    # ld>0 且 ld>hd, 则mm=ld, 否则为0
    _df['mm'] = _df.apply(lambda x: x.ld if x.ld > 0 and x.hd < x.ld else 0, axis=1)
    # 上升趋向mp的n日之和
    _df['dmp'] = _df.mp.rolling(window1).sum()
    # 下降趋向mm的n日之和
    _df['dmm'] = _df.mm.rolling(window1).sum()

    # 上升趋向指数pdi = dmp / trz * 100
    _df['pdi'] = _df.dmp / trz * 100
    # 下降趋向指数mdi = dmm / trz * 100
    _df['mdi'] = _df.dmm / trz * 100
    # 平均趋向指标adx = abs(pdi - mdi) / (pdi + mdi)
    _df['adx'] = ((_df.mdi - _df.pdi).abs() / (_df.mdi + _df.pdi) * 100).rolling(window2).mean()
    # adxr平均趋向指标比例 = (今日adx + m日前adx) / 2
    _df['adxr'] = (_df.adx + _df.adx.shift(window2)) / 2
    # dmi = pdi - mdi
    _df['dmi'] = _df.pdi - _df.mdi
    return _df['dmi']


# 能量潮
def OBV(df):
    return (((df.close.diff(1).fillna(0) >= 0) * 2 - 1) * df.vol).cumsum()


# 移动能量潮
def SMOBV(df, window):
    return OBV(df).rolling(window).mean()
