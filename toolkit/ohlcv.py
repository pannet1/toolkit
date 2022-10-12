import pandas as pd
from enum import Enum
import logging


class CandleType(Enum):
    BULL = 1
    BEAR = -1
    DOJI = 0


class Ohlcv:
    def __init__(self, rel_path_file="data/ticks.csv"):
        self.rel_path_file = rel_path_file
        self.df = pd.DataFrame()

    def get_candles(self):
        return self.df

    def candle(self, idx: int):
        idx = idx * -1
        return self.df.iloc[[idx]]

    def candle_type(self, idx):
        can = self.candle(idx)
        if can["close"].values[0] > can["open"].values[0]:
            return CandleType.BULL
        elif can["close"].values[0] < can["open"].values[0]:
            return CandleType.BEAR
        else:
            return CandleType.DOJI

    def len(self):
        return len(self.df.index)

    def ohlcv_val(self, idx: int, ohlcv: str) -> float:
        can = self.candle(idx)
        return can[ohlcv].values[0]

    def get_ltp(self):
        pass


class Candlestick(Ohlcv):
    def __init__(self, obj):
        super().__init__()
        ticks = pd.read_csv(
            self.rel_path_file,
            names=["Date", "Symbol", "ltp"],
            index_col=0,
            parse_dates=True,
        ).dropna()
        comp = obj["base_script"].split(":")
        filtered = ticks.loc[ticks["Symbol"] == comp[1]]
        timed = filtered.between_time(obj["tick_start"], obj["tick_end"])
        self.df = timed["ltp"].resample(obj["timeframe"]).ohlc().dropna()
        logging.info(self.df)

    def get_ltp(self):
        if self.len() > 0:
            ltp = self.df['close'].values[0]
        else:
            ltp = None
        return ltp


class Heikenashi(Ohlcv):
    def __init__(self, obj):
        ca = Candlestick(obj)
        df = ca.get_candles()
        self.ltp = None
        if len(df) > 2:
            df["c"] = (df["open"] + df["high"] + df["low"] + df["close"]) / 4
            df["o"] = ((df["open"] + df["close"]) / 2).shift(1)
            df.iloc[0, -1] = df["o"].iloc[1]
            df["h"] = df[["high", "o", "c"]].max(axis=1)
            df["l"] = df[["low", "o", "c"]].min(axis=1)
            df["open"], df["high"], df["low"], df["close"] = (
                df["o"],
                df["h"],
                df["l"],
                df["c"],
            )
            df.drop(["o", "h", "l", "c"], axis=1, inplace=True)
            self.df = df
            logging.info(df)
            self.ltp = ca.get_ltp()
        else:
            self.df = pd.DataFrame()

    def get_ltp(self):
        return self.ltp
