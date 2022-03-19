import os

class Config:
    API_ID = int( os.getenv("api_id","1234") )
    API_HASH = os.getenv("api_hash","21ab7cb0a453b5e60016dc7bbeb71cb")
    CHANNEL = int( os.getenv("channel_files_chat_id","-1001601419165") )
    CHANNEL_USERNAME = os.getenv("channel_username","UserLandapp")
    TOKEN = os.getenv("token","1408542385:AAEatXPbSubsYmlW8kPTUAr")
    DOMAIN  = os.getenv("domain","http://localhost")