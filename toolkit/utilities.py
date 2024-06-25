from datetime import datetime as dt
from time import sleep


class Utilities:
    def __init__(self):
        self.secs = 1

    def slp_til_nxt_sec(self) -> None:
        secs = dt.now().second
        if secs == dt.now().second:
            t = round(dt.now().microsecond / 1000000, 2)
            sleep(t)

    def slp_for(self, sec=1) -> None:
        sleep(sec)

    def pkg_mgr(self):
        try:
            from rich import print
        except ImportError:
            # Module is not installed, attempt to install it
            import subprocess
            import sys

            # Replace 'your_module' with the actual module name you want to install
            module_name = "rich"

            # Use 'pip' to install the module
            try:
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "install", module_name]
                )
            except subprocess.CalledProcessError:
                print(f"Failed to install {module_name}. Please install it manually.")
            else:
                # Module installed successfully, now you can import it
                from rich import print
