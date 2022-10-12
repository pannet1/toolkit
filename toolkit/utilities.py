from datetime import datetime as dt
from time import sleep


class Utilities:
    def slp_til_nxt_sec(self):
        secs = dt.now().second
        while secs == dt.now().second:
            t = dt.now()
            sleep(t.microsecond / 1000000)
