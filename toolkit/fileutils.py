import os
import sys
import yaml
import json
import csv
from datetime import date as d, datetime as dt
import pandas as pd
from typing import Any, List, NoReturn


class Fileutils:
    def __init__(self, data="./data/"):
        self.data = data

    def get_file_extension(self, filepath: str) -> str:
        # Split the file path into base and extension
        _, extension = os.path.splitext(filepath)
        # Return the extension (without the period)
        return extension[1:] if extension else ""

    # file
    def is_file_exists(self, filepath: str) -> bool:
        if os.path.exists(filepath):
            return True
        return False

    def read_file(self, filepath: str):
        try:
            extn = self.get_file_extension(filepath)
            with open(filepath, "r") as file:
                if extn in ["yml", "yaml"]:
                    data = yaml.safe_load(file)
                elif extn == "json":
                    data = json.load(file)
                else:
                    print(f"unknown {extn=}")
                    data = file.read()
                return data
        except Exception as e:
            print(f"{filepath} not found {e}")

    def write_file(self, filepath, content) -> None:
        try:
            extn = self.get_file_extension(filepath)
            if extn == "json":
                json_str = json.dumps(
                    content, ensure_ascii=False, indent=4, default=str)
                with open(filepath, "w", encoding="utf-8") as outfile:
                    outfile.write(json_str)
            else:
                with open(filepath, "w") as file:
                    file.write(content)
        except Exception as e:
            print(f"write file {e}")

    def del_file(self, filepath: str) -> None:
        try:
            os.remove(filepath)
        except Exception as e:
            print(f"{e} while del file")

    def nuke_file(self, filepath: str) -> NoReturn:
        try:
            with open(filepath, "w"):
                pass
        except Exception as e:
            print(f"{e} while nuke {filepath}")

    def add_path(self, inserted_path: str):
        curr_path = os.path.realpath(os.path.dirname(__file__))
        sys.path.insert(0, curr_path + inserted_path)

    def is_file_not_2day(self, filepath: str) -> bool:
        path, _ = os.path.split(filepath)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"{path} not found ... creating")

        if not os.path.exists(filepath):
            with open(filepath, "w") as file:
                file.write("")
            print(f"file {filepath} created")
            bln_state = True
        else:
            ts = os.path.getmtime(filepath)
            timestamp_date = dt.fromtimestamp(ts).date()

            bln_state = False if (timestamp_date.year == d.today().year and
                                  timestamp_date.month == d.today().month and
                                  timestamp_date.day == d.today().day) else True

            print(f"{bln_state}: {timestamp_date} == {d.today()}")
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

    def on_subfolders(self, filepath) -> List:
        if os.path.exists(filepath):
            # Use os.listdir to get a list of all items in the directory
            items = os.listdir(filepath)
            # Use a list comprehension to filter out only the directories (folders)
            folders = [
                item for item in items if os.path.isdir(os.path.join(filepath, item))
            ]
            return folders
        else:
            os.makedirs(filepath)
            return []

    # returns list of files names with specified extension
    def get_files_with_extn(self, extn: str, diry: str) -> List:
        lst = []
        for f in os.listdir(diry):
            if len(extn) > 0 and not f.endswith("." + extn):
                continue
            lst.append(f)
        return lst

    # yaml
    def get_lst_fm_yml(self, filepath: str) -> Any:
        try:
            with open(filepath, "r") as f:
                lst = yaml.safe_load(f)
            return lst
        except Exception as e:
            print(f"{filepath} not found {e}")

    # json
    def json_fm_file(self, filepath) -> Any:
        obj = False
        extn = self.get_file_extension(filepath)
        if extn != "json":
            filepath = filepath + "." + extn
        with open(filepath, "r") as infile:
            obj = json.load(infile)
        return obj

    # csv
    def append_to_csv(self, csv_file, lst_row):
        extn = self.get_file_extension(csv_file)
        if extn != "csv":
            csv_file = csv_file + "." + extn
        with open(csv_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(lst_row)

    def get_df_fm_csv(self, subfolder, csv_file, colnames=[]):
        extn = ".csv"
        if csv_file.endswith(extn) is False:
            csv_file = csv_file + extn
        df = pd.read_csv(filepath_or_buffer=subfolder + "/" + csv_file,
                         names=colnames,
                         header=None
                         )
        return df

    def xls_to_dict(self, filepath: str):
        """
        filepath
            Excel file in required xls format with each one row for items
        """
        xls = pd.read_excel(filepath).to_dict(orient="records")
        return xls


if __name__ == "__main__":
    obj = Fileutils()
    dtime = obj.get_file_mtime("../../../spread.db")
    print(dtime)
