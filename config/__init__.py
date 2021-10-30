import os

class Config:
    API_ID = int( os.getenv("api_id","1234") )
    API_HASH = os.getenv("api_hash","21ab7cb0a453b5e60016dc7bbeb701cb")
    CHANNEL = int( os.getenv("channel_files_chat_id","-1001249461809") )
    CHANNEL_USERNAME = os.getenv("channel_username","UserLandapp")
    TOKEN = os.getenv("token","xxxxx")
    DOMAIN  = os.getenv("domain","https://newdlstar.herokuapp.com")