import os
from dotenv import load_dotenv

# Load environment from .env
load_dotenv()

DATABASE_URI = os.getenv("LOGGING_DATABASE_URI")
