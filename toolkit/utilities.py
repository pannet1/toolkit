from datetime import datetime as dt
from time import sleep


class Utilities:

    def __init__(self):
        self.t = 1
        self._reset()

    def _reset(self) -> None:
        self.slp = 1

    def slp_til_nxt_sec(self) -> None:
        secs = dt.now().second
        while secs == dt.now().second:
            t = dt.now().microsecond / 1000000
            print(f"sleeping for {t} seconds")
            sleep(t)
        self.slp += t

    def slp_for(self, sec=1) -> None:
        sleep(sec)
        self.reset()
