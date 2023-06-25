from datetime import datetime as dt
from time import sleep
from typing import Typing

class Utilities:

    def __init__(self):
        self.t = 1
        self._reset()

    def _reset(self)
        self.slp = 1

    def slp_til_nxt_sec(self):
        secs = dt.now().second
        while secs == dt.now().second:
            t = dt.now().microsecond / 1000000
            print(f"sleeping for {t} seconds")
            sleep(t)
        self.slp += t

    def slp_for(self, sec=1):
        sleep(sec)
        self.reset()

