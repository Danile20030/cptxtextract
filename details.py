import os
from os import getenv

# Required variables with error handling
try:
    API_ID = int(os.environ["API_ID"])  # Will raise KeyError if missing
    API_HASH = os.environ["API_HASH"]
    BOT_TOKEN = os.environ["BOT_TOKEN"]
    OWNER_ID = int(os.environ.get("OWNER_ID", 0))  # Optional with default
    SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "").split()))
    CHANNEL_ID = os.environ.get("CHANNEL_ID", "")
    
    # Validation
    if not all([API_ID, API_HASH, BOT_TOKEN]):
        raise ValueError("Missing required environment variables")

except (KeyError, ValueError) as e:
    print(f"❌ Configuration Error: {str(e)}")
    print("Please check your Railway environment variables!")
    exit(1)
