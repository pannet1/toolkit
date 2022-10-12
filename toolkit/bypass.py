import pyotp
from kiteext import KiteExt
import logging


def Bypass(broker):
    try:
        otp = pyotp.TOTP(broker["totp"])
        pin = otp.now()
        pin = f"{int(pin):06d}"
        kite = KiteExt()
        kite.login_with_credentials(
            userid=broker["username"], password=broker["password"], pin=pin
        )
        return kite
    except Exception as e:
        logging.critical(f"{e} unable to login")
        exit()
