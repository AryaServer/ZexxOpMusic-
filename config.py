from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/e804e7958085fd80188fd.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/ce3526800b3bdb61bca7d.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+rgFqoc9--2ZhNzA9")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Arya_server")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6495765183").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
