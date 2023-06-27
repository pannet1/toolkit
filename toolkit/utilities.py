from datetime import datetime as dt
from time import sleep


class Utilities:

    def __init__(self):
        self.secs = 1

    def slp_til_nxt_sec(self) -> None:
        secs = dt.now().second
        if secs == dt.now().second:
            t = round(secs.microsecond / 1000000, 2)
            print(f"sleeping for {t} seconds")
            sleep(t)

    def slp_for(self, sec=1) -> None:
        sleep(sec)
