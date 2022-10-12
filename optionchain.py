from logger import Logger
import re


class Oc:

    def __init__(self):
        self.log = Logger()

    def _get_option(self, script_name, options):
        scr = ''
        for o in options:
            if script_name.find(o) > -1:
                scr = o
        return scr

    def _ce_or_pe(self, script_name):
       ce_or_pe = 0
       if script_name.find('PE') > -1:
            ce_or_pe = -1
       elif script_name.find('CE') > -1:
            ce_or_pe = 1
       self.log.info(f'call or put is:  {ce_or_pe}')
       return ce_or_pe
    
    def get_scr_param(self, script_name, options):
        lst = []
        moneyness = ['ITM', 'OTM']
        # return word found within brackets
        ness = script_name[script_name.find('(')+1 : script_name.find(')') ]
        if ness in moneyness:
           ce_or_pe = self._ce_or_pe(script_name)
           if ce_or_pe == 1 or ce_or_pe == -1:
                scr = self._get_option(script_name, options)                
                lst = [scr, ness, ce_or_pe]
        return lst

    def get_tradingsymbol(self, df, lst, ltp, script_name):
        strike = 0
        df['differs'] = df['strikes']-ltp
        pos_df = df.loc[(df['differs'].shift() <= 0) & (df['differs'] >= 0)]
        self.log.info(pos_df)
        pos_strike = pos_df['strikes'].values[0]
        neg_strike_index = pos_df.index - 1
        neg_strike = df.loc[neg_strike_index]['strikes'].values[0]
        # PE
        if lst[2] == -1:
            strike = str(pos_strike) if lst[1] == 'ITM' else str(neg_strike)
        # CE
        else:
            strike = str(pos_strike) if lst[1] == 'OTM' else str(neg_strike)
        trade_sym = re.sub(r'\(.+\)', strike, script_name)
        self.log.info(f"trading symbol  {trade_sym}")
        return trade_sym
