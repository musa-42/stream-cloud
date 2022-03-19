from telethon import TelegramClient
from telethon.sessions import StringSession
from . import Router
from config import Config

class Client(Config, Router):
    bot_token = Config.TOKEN
    
    def __init__(self):
        self.client = TelegramClient(
            StringSession(),
            self.API_ID,
            self.API_HASH,
            # proxy=("socks5","127.0.0.1",9050)
         )
    
    @staticmethod
    def get_file_name(message):
        if message.file.name:
            return message.file.name
        ext = message.file.ext or ""
        return f"file{ext}"