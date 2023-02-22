from .fileutils import Fileutils
from toolkit.optionchain import Oc
import logging


class Symbols:
    def __init__(self):
        self.oc = Oc()
        self.futils = Fileutils()
        # get option chain names from strikes directory
        oc_files = self.futils.get_files_with_extn("csv", "strikes/")
        self.options = []
        for fname in oc_files:
            f = fname.rsplit(".")
            self.options.append(f[0])
        logging.info('f{self.options}')

    def set_trd_sym(self, side, obj):
        if side == "B":
            script = obj["buy_script"]
        else:
            script = obj["sell_script"]

        params = self.oc.get_scr_param(script, self.options)
        if params:
            # split option script, moneyness, ce_or_pe
            strk_lst = self.futils.get_df_fm_csv("strikes", params[0], ["strikes"])
            sym = self.oc.get_tradingsymbol(strk_lst, params, obj["ltp"], script)
        else:
            sym = script

        return sym
