  
from dotenv import load_dotenv
import os


load_dotenv()

db_location = os.getenv("VIBER_DB_LOCATION",None)
tg_token = os.getenv("TG_BRIDGE_TOKEN",None)