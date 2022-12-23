from typing import Dict


class Datastruct:
    def fltr_dct_by_key(self, dct: Dict, lst) -> Dict:
        """
        generic function to filter any dict
        """
        dct_filter = {}
        for k, v in dct.items():
            if k in lst:
                dct_filter[k] = v
        return dct_filter
