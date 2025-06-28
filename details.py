import os
from os import getenv


API_ID = int(getenv("API_ID", ))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "7320087240"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7320087240").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://daxxop:daxxop@daxxop.dg3umlc.mongodb.net/?retryWrites=true&w=majority")
CHANNEL_ID = int(getenv("CHANNEL_ID", "8118953747"))
