from datetime import time, date
from pydantic import BaseModel

class Scripts(BaseModel):
    base_script: str
    trade_exch: str
    buy_script: str
    buy_tx: str
    sell_script: str
    sell_tx: str
    timeframe: str
    entry_start: time
    entry_end: time
    square_off: time
    product: str
    quantity: int
    tick_start: time
    tick_end: time

class Strikes(BaseModel):
    base_script: str
    base_exch: str
    sample: int
    addsub: int
    expiry: str


