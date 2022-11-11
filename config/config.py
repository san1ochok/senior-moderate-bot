import os
from dotenv import load_dotenv

load_dotenv()

ADMIN = os.getenv("ADMIN_ID")
GROUP = os.getenv("GROUP_ID")
TOKEN = os.getenv("AUTH_TOKEN")
DATABASE = os.getenv("DATABASE")
MONGO_URI = os.getenv("AUTH_TOKEN")


PARSE_MODE = 'Markdown'



