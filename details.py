import os
from os import getenv


API_ID = int(getenv("API_ID", 21702398))
API_HASH = getenv("API_HASH", "70b0cc4ab3e1f29aa2d386883adeda38")
BOT_TOKEN = getenv("BOT_TOKEN", "8118953747:AAH_F8eClQ6C_x1j0SHU1g_7b-Xfw6M_2JU")
OWNER_ID = int(getenv("OWNER_ID", "7320087240"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7320087240").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://daxxop:daxxop@daxxop.dg3umlc.mongodb.net/?retryWrites=true&w=majority")
CHANNEL_ID = int(getenv("CHANNEL_ID", "8118953747"))
