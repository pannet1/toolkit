from datetime import date as d
import os, sys
import yaml, json
from typing import List, Optional
import pandas as pd
import logging


class Fileutils:
    def __init__(self, scr="scripts/"):
        self.scr = scr

    def add_path(self, inserted_path: str):
        curr_path = os.path.realpath(os.path.dirname(__file__))
        sys.path.insert(0, curr_path + inserted_path)

    def get_lst_fm_yml(self, relpath: str) -> List:
        try:
            with open(relpath, "r") as f:
                lst = yaml.safe_load(f)
            return lst
        except FileNotFoundError:
            logging.warning(f"{ relpath } file not found")

    # returns list of files names with specified extension
    def get_files_with_extn(self, extn: str, diry: Optional[str] = None) -> List:
        if not diry:
            diry = self.scr
        lst = []
        for f in os.listdir(diry):
            if f.endswith("." + extn):
                lst.append(f)
        return lst

    # json
    def save_file(self, jsonobj, fname):
        with open(fname + ".json", "w", encoding="utf-8") as outfile:
            json.dump(jsonobj, outfile, ensure_ascii=False, indent=4)

    def json_fm_file(self, fname):
        obj = False
        with open(fname + ".json", "r") as infile:
            obj = json.load(infile)
        return obj

    # csv
    def get_df_fm_csv(self, subfolder, csv_file, colnames=[]):
        df = pd.read_csv(
            subfolder + "/" + csv_file + ".csv", names=colnames, header=None
        )
        return df

    def is_file_not_2day(self, filepath: str) -> bool:
        try:
            if os.path.exists(filepath):
                ts = os.path.getmtime(filepath)
                fd = d.fromtimestamp(ts)
                if fd == d.today():
                    return False
            else:
                return True
        except FileNotFoundError:
            logging.warning(f"{filepath} file not found")

    def xls_to_dict(self, filename: str):
        """
        filename
            Excel file in required xls format with each one row for items
        """
        xls = pd.read_excel(filename).to_dict(orient='records')
        return xls

