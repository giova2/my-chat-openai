import os

HARD_CODED_USERNAME = os.getenv("HARD_CODED_USERNAME")
HARD_CODED_PASSWORD = os.getenv("HARD_CODED_PASSWORD")

def authorize_user(username: str, password: str) -> bool:
    if username == HARD_CODED_USERNAME and password == HARD_CODED_PASSWORD:
        return True
    else:
        return False