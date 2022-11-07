import os
from dotenv import load_dotenv

load_dotenv()

admin = os.getenv("ADMIN_ID")
group = os.getenv("GROUP_ID")
token = os.getenv("AUTH_TOKEN")
parse_mode = 'Markdown'



