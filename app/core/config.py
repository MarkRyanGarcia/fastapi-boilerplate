import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://user:password@localhost/dbname",
)
CLERK_SECRET_KEY = os.getenv("CLERK_SECRET_KEY", "sk-...")
DEBUG = os.getenv("DEBUG", "").lower() in ("true", "1", "yes")