import requests as r
from typing import NoReturn
"""
https://core.telegram.org/bots/features#creating-a-new-bot
https://www.shellhacks.com/telegram-api-send-message-personal-notification-bot/
"""

base_url = "https://api.telegram.org/"


class Telegram:

    def __init__(self, api_key: str, chat_id: int = 0):
        self.api_key = api_key
        self.chat_id = chat_id
        self.last_msg = ""

    def set_chat_id(self) -> NoReturn:
        url = f"{base_url}bot{self.api_key}/getUpdates"
        print(url)
        if self.chat_id == 0:
            resp = r.get(url)
            if resp:
                self.chat_id = resp.json().get("result")[0].get(
                    "message").get("chat").get("id")
                print("chat_id is {self.chat_id}")

    def send_msg(self, msg: str) -> NoReturn:
        url = f"{base_url}bot{self.api_key}/sendMessage?chat_id={self.chat_id}&text="
        resp = r.get(url+msg)
        if resp:
            self.last_msg = resp.json().get("result").get("text")


if __name__ == "__main__":
    api_key = ""
    if len(api_key) > 5:
        tgram = Telegram(api_key, 0)
        print("message to your bot after /start")
        time = __import__("time")
        time.sleep(60)
        yaml = __import__("yaml")
        tgram.get_chat_id()
        dct = {"api_key": tgram.api_key, "chat_id": tgram.chat_id}
        with open("telegram.yaml") as cred:
            yaml.dump(dct, cred)
    else:
        print("get api key and rerun this")
