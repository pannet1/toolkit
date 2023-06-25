from datetime import datetime as dt
from time import sleep
from typing import Typing

class Utilities:

    def __init__(self):
        self.reset()

    def reset(self)
        self.slp = 1

    def slp_til_nxt_sec(self):
        self.t = 1
        secs = dt.now().second
        while secs == dt.now().second:
            self.t = dt.now().microsecond / 1000000
            sleep(self.t)
        self.slp += self.t

    def slp_for(self, sec=1):
        sleep(sec)

