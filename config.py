import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "demo_key")