import os
import sys
import yaml
import json
import csv
from datetime import date as d, datetime as dt
from typing import List, Optional
import pandas as pd


class Fileutils:
    def __init__(self, scr="scripts/"):
        self.scr = scr
    
    # file 
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

        path, _ = os.path.split(filepath)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"{path} not found {e}")

        if not os.path.exists(filepath):
            with open(filepath, 'w') as file:
                file.write("")
            print(f"file {filepath} created")
            bln_state = True
        else:
            ts = os.path.getmtime(filepath)
            bln_state = False if (d.fromtimestamp(ts)
                                  == d.today()) else True
            print(f"{bln_state}: {d.fromtimestamp(ts)} == {d.today()}")
        return bln_state

    def get_file_mtime(self, filepath: str) -> str:
        try:
            ts = os.path.getmtime(filepath)
            return dt.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
        except FileNotFoundError as e:
            print(f"{filepath} not found {e}")
            return "file_not_found"
        except Exception as e:
            print(e)
            return "file_not_found"

    def on_subfolders(self, filepath):
        if os.path.exists(filepath):
            # Use os.listdir to get a list of all items in the directory
            items = os.listdir(filepath)
            # Use a list comprehension to filter out only the directories (folders)
            folders = [item for item in items if os.path.isdir(os.path.join(filepath, item))]
            return folders
        else:
            os.makedirs(filepath)
            return []
            
    # returns list of files names with specified extension
    def get_files_with_extn(self, extn: str, diry: str) -> List:
        lst = []
        for f in os.listdir(diry):
            if len(extn)>0 and not f.endswith("." + extn):
                continue
            lst.append(f)
        return lst

    # yaml
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

    def append_to_csv(self, filepath, lst_row):
        # Open the CSV file in append mode and write the new row
        with open(filepath, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(lst_row)

    def xls_to_dict(self, filename: str):
        """
        filename
            Excel file in required xls format with each one row for items
        """
        xls = pd.read_excel(filename).to_dict(orient='records')
        return xls


if __name__ == "__main__":
    obj = Fileutils()
    dtime = obj.get_file_mtime("../../../spread.db")
    print(dtime)
