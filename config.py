
import re
from os import environ 

id_pattern = re.compile(r'^.\d+$')

AUTH_CHANNEL = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('AUTH_CHANNEL', '').split()] 
# give channel id with separate space. Ex: ('-10073828 -102782829 -1007282828')


class Config:
    API_ID = int(environ.get("API_ID", "23621595"))
    API_HASH = environ.get("API_HASH", "de904be2b4cd4efe2ea728ded17ca77d")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7736867939:AAF5ukBIKHDt39sirL2p2cETKX2xPXRhtG8") 
    BOT_SESSION = environ.get("BOT_SESSION", "PrimeXBots") 
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://mageerauldvjo8d:O3cGzJqMo1e5YVXA@cluster0.wdeqnro.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER = int(environ.get("BOT_OWNER", "1249672673"))



class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []




