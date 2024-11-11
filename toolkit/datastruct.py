from typing import Dict, List


def filter_dictionary_by_keys(elephant: Dict, keys: List) -> Dict:
    """
    generic function to filter any dict
    """
    if not any(elephant):
        return elephant

    dct_filter = {}
    for k, v in elephant.items():
        if k in keys:
            dct_filter[k] = v
    return dct_filter
