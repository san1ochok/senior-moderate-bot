import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("AUTH_TOKEN"))
