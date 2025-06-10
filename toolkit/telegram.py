import requests as r
from toolkit.fileutils import Fileutils


base_url = "https://api.telegram.org/"


class Telegram:
    """
    https://core.telegram.org/bots/features#creating-a-new-bot
    https://www.shellhacks.com/telegram-api-send-message-personal-notification-bot/
    """

    def __init__(self, api_key: str, chat_id: int = 0):
        self.api_key = api_key
        self.chat_id = chat_id
        self._last_msg = ""
        if self.chat_id == 0:
            self._set_chat_id()

    def _set_chat_id(self):
        print("add the bot to your group and send a test message")
        __import__("time").sleep(180)
        url = f"{base_url}bot{self.api_key}/getUpdates"
        resp = r.get(url)
        try:
            self.chat_id = (
                resp.json().get("result")[0].get("message").get("chat").get("id")
            )
        except Exception as e:
            print(f"Unable to set chat id due to {e}")

    def send_msg(self, msg):
        try:
            if isinstance(msg, dict):
                url = f"{base_url}bot{self.api_key}/sendMessage?chat_id={self.chat_id}"
                data = {"text": str(msg)}
                resp = r.post(url, data=data)
                if resp:
                    self._last_msg = resp.json().get("result").get("text")
            else:
                url = f"{base_url}bot{self.api_key}/sendMessage?chat_id={self.chat_id}&text="
                resp = r.get(url + msg)
                if resp:
                    self._last_msg = resp.json().get("result").get("text")
        except Exception as e:
            print(f"{e} while sending message")
            self._set_chat_id()

    @property
    def last_msg(self):
        return self._last_msg
