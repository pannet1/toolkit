import requests as r
from typing import NoReturn
from toolkit.fileutils import Fileutils


base_url = "https://api.telegram.org/"


class Telegram:
    """
    https://core.telegram.org/bots/features#creating-a-new-bot
    https://www.shellhacks.com/telegram-api-send-message-personal-notification-bot/
    """

    def __init__(self, api_key: str, chat_id: int = 0, fpath: str = "./"):
        self.api_key = api_key
        self.chat_id = chat_id
        self.last_msg = ""
        self._set_chat_id(fpath)

    def _set_chat_id(self, fpath: str) -> NoReturn:
        futils = Fileutils()
        url = f"{base_url}bot{self.api_key}/getUpdates"
        print(url)
        if self.chat_id == 0:
            if futils.is_file_exists(f"{fpath}/.telegram"):
                self.chat_id = futils.read_file(f"{fpath}/.telegram")

        if not self.chat_id:
            print("message to your bot after /start")
            time = __import__("time")
            time.sleep(60)
            resp = r.get(url)
            if resp:
                self.chat_id = (
                    resp.json().get("result")[0].get("message").get("chat").get("id")
                )
                print("going to write chat_id {self.chat_id}")
            if self.chat_id:
                futils.write_file(f"{fpath}/.telegram", str(self.chat_id))

    def send_msg(self, msg: str) -> NoReturn:
        url = f"{base_url}bot{self.api_key}/sendMessage?chat_id={self.chat_id}&text="
        resp = r.get(url + msg)
        if resp:
            self.last_msg = resp.json().get("result").get("text")
