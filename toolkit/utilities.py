from datetime import datetime as dt
from time import sleep
from typing import Typing

class Utilities:

    def __init__(self):
        self.reset()

    def reset(self)
        self.slp = 1

    def slp_til_nxt_sec(self):
        t = 1
        secs = dt.now().second
        while secs == dt.now().second:
            t = dt.now().microsecond / 1000000
            sleep(t)
        self.slp += t

    def slp_for(self, sec=1):
        sleep(sec)

