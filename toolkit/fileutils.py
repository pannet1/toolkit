import os
import sys
import yaml
import json
from datetime import date as d
from typing import List, Optional
import pandas as pd


class Fileutils:
    def __init__(self, scr="scripts/"):
        self.scr = scr

    def del_file(self, filename):
        if os.path.exists(filename):
            os.remove(filename)
            print(f"{filename} file removed")
        else:
            print(f"{filename} does not exist")

    def nuke_file(self, relpath):
        try:
            with open(relpath, "w"):
                pass
        except FileNotFoundError as e:
            print(f"{relpath} not found {e}")

    def add_path(self, inserted_path: str):
        curr_path = os.path.realpath(os.path.dirname(__file__))
        sys.path.insert(0, curr_path + inserted_path)

    def is_file_not_2day(self, filepath: str) -> bool:
        try:
            path, filename = os.path.split(filepath)
            if not os.path.exists(path):
                os.makedirs(path)

            if not os.path.exists(filepath):
                # Create the file
                with open(filepath, 'w') as file:
                    file.write("")
                print(f"File '{filename}' created in '{path}'.")
                return True
            else:
                ts = os.path.getmtime(filepath)
                bln_state = False if (d.fromtimestamp(ts)
                                      == d.today()) else True
                return bln_state
        except FileNotFoundError as e:
            print(f"{filepath} not found {e}")

    def get_file_mtime(self, filepath: str) -> str:
        try:
            ts = os.path.getmtime(filepath)
            return d.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
        except FileNotFoundError as e:
            print(f"{filepath} not found {e}")
            return "file_not_found"
        except Exception as e:
            print(e)
            return "file_not_found"

    # returns list of files names with specified extension
    def get_files_with_extn(self, extn: str, diry: Optional[str] = None) -> List:
        if not diry:
            diry = self.scr
        lst = []
        for f in os.listdir(diry):
            if f.endswith("." + extn):
                lst.append(f)
        return lst

    # yaml file utilities
    def get_lst_fm_yml(self, relpath: str) -> List:
        try:
            with open(relpath, "r") as f:
                lst = yaml.safe_load(f)
            return lst
        except FileNotFoundError as e:
            print(f"{relpath} not found {e}")

    # json

    def save_file(self, jsonobj, fname):
        with open(fname + ".json", "w", encoding="utf-8") as outfile:
            json.dump(jsonobj, outfile, ensure_ascii=False, indent=4, str=str)

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

    def xls_to_dict(self, filename: str):
        """
        filename
            Excel file in required xls format with each one row for items
        """
        xls = pd.read_excel(filename).to_dict(orient='records')
        return xls
