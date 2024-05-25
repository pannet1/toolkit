import os
import sys
import yaml
import json
import csv
from datetime import date as d, datetime as dt
import pandas as pd
from typing import Any, List, NoReturn
import shutil


class Fileutils:
    def __init__(self, data="../data/"):
        self.data = data

    def copy_file(self, source_dir="../", destination_dir="", filename="settings.yml"):
        if destination_dir == "":
            destination_dir = self.data
        source_path = os.path.join(source_dir, filename)
        destination_path = os.path.join(destination_dir, filename)

        try:
            shutil.copy(source_path, destination_path)
            print(
                f"File '{filename}' copied successfully from {source_dir} to {destination_dir}."
            )
        except FileNotFoundError:
            print(f"File '{filename}' not found in {source_dir}.")
        except PermissionError:
            print(f"Permission denied while copying '{filename}'.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_file_extension(self, filepath: str) -> str:
        # Split the file path into base and extension
        _, extension = os.path.splitext(filepath)
        # Return the extension (without the period)
        return extension[1:] if extension else ""

    # file
    def is_file_exists(self, filepath: str) -> bool:
        if os.path.exists(filepath):
            return True
        else:
            _ = self.is_mk_filepath(filepath)
            return False

    def read_file(self, filepath: str):
        try:
            extn = self.get_file_extension(filepath)
            if extn in ["yml", "yaml"]:
                with open(filepath, "r") as file:
                    data = yaml.safe_load(file)
                    return data

            elif extn == "json":
                with open(filepath, "r", encoding="utf-8", newline="") as file:
                    data = json.load(file)
                    return data

            else:
                with open(filepath, "r") as file:
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
                    content, ensure_ascii=False, indent=4, default=str
                )
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

    def is_mk_filepath(self, filepath: str) -> bool:
        try:
            path, _ = os.path.split(filepath)
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"{path} not found ... creating")

            if not os.path.exists(filepath):
                with open(filepath, "w") as file:
                    file.write("")
                print(f"file {filepath} created")
        except Exception as e:
            print(f"Error while mk filepath: {e}")
            return False
        return True

    def is_file_not_2day(self, filepath: str) -> bool:
        if not self.is_file_exists(filepath):
            bln_state = True
        else:
            ts = os.path.getmtime(filepath)
            timestamp_date = dt.fromtimestamp(ts).date()

            bln_state = (
                False
                if (
                    timestamp_date.year == d.today().year
                    and timestamp_date.month == d.today().month
                    and timestamp_date.day == d.today().day
                )
                else True
            )
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

    def rename(self, old_folder_path, new_folder_name):
        """
        Args:
            old_folder_path: folder name with full path
            new_folder_name: new folder name
        """
        try:
            path, _ = os.path.split(old_folder_path)
        except FileNotFoundError as e:
            print(f"{old_folder_path} not found {e}")
            return None

        try:
            os.rename(old_folder_path, path + "/" + new_folder_name)
            print("Folder renamed successfully.")
        except FileNotFoundError:
            print("Folder not found.")
        except FileExistsError:
            print("A folder with the new name already exists.")
        except Exception as e:
            print("An error occurred:", e)

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
        df = pd.read_csv(
            filepath_or_buffer=subfolder + "/" + csv_file, names=colnames, header=None
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
    t = "./tests"
    if obj.is_file_not_2day(t):
        dtime = obj.get_file_mtime(t)
        # convert string to date
        test = dtime.split(" ")[0].replace("-", "")
        obj.rename(t, test)
