import os
from pyrogram import Client
#from plugins import *

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
SESSION = os.environ["SESSION_STRING"]

adi = Client(
    SESSION,
    api_id=API_ID,
    api_hash=API_HASH
)
