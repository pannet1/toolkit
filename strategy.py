from logger import Logger
from ohlcv import Heikenashi, CandleType


class HaBreakout:
    def __init__(self, obj):
        self.log = Logger()
        self.ha = Heikenashi(obj)
        self.ltp = self.ha.get_ltp()

    def cond(self):
        cond = 0
        if self.ha.len() > 1:
            c_open = self.ha.ohlcv_val(1, "open")
            p_high = self.ha.ohlcv_val(2, "high")
            p_low = self.ha.ohlcv_val(2, "low")
            if (
                self.ha.candle_type(2) == CandleType.BULL
                and self.ha.candle_type(1) == CandleType.BEAR
                and c_open < p_low
            ):
                cond = 1
                self.log.info("BUY signal")
            elif (
                self.ha.candle_type(2) == CandleType.BEAR
                and self.ha.candle_type(1) == CandleType.BULL
                and c_open > p_high
            ):
                cond = -1
                self.log.info("SELL signal")

        return cond
