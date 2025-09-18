import os
import sys
import logging
from instagrapi import Client

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

USERNAME = os.environ.get("IG_USERNAME") or os.environ.get("INSTAGRAM_USERNAME")
PASSWORD = os.environ.get("IG_PASSWORD") or os.environ.get("INSTAGRAM_PASSWORD")
FRIEND = os.environ.get("FRIEND_USERNAME")
MESSAGE = os.environ.get("MESSAGE", "Good Morning 🌞")

if not USERNAME or not PASSWORD or not FRIEND:
    logging.error("Missing env vars. Set IG_USERNAME, IG_PASSWORD, and FRIEND_USERNAME in GitHub Secrets.")
    sys.exit(1)

cl = Client()
try:
    logging.info("Logging in as %s", USERNAME)
    cl.login(USERNAME, PASSWORD)
except Exception as e:
    logging.exception("Login failed. Instagram may ask for verification or 2FA.")
    sys.exit(2)

try:
    friend_id = cl.user_id_from_username(FRIEND)
    logging.info("Found friend %s -> id %s", FRIEND, friend_id)
except Exception as e:
    logging.exception("Could not find friend username.")
    sys.exit(3)

try:
    cl.direct_send(MESSAGE, [friend_id])
    logging.info("Message sent to %s", FRIEND)
except Exception as e:
    logging.exception("Failed to send DM.")
    sys.exit(4)
