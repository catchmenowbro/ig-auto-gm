import os
import sys
import logging
from instagrapi import Client

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")
FRIEND = os.getenv("FRIEND_USERNAME")
MESSAGE = os.getenv("MESSAGE", "Good Morning 🌞")

if not USERNAME or not PASSWORD or not FRIEND:
    logging.error("Missing env vars. Set IG_USERNAME, IG_PASSWORD and FRIEND_USERNAME in repo Secrets.")
    sys.exit(1)

cl = Client()

# Optional: if a session file was written to insta_settings.json by the workflow, load it
if os.path.exists("insta_settings.json"):
    try:
        cl.load_settings("insta_settings.json")
        logging.info("Loaded saved session (insta_settings.json).")
    except Exception as e:
        logging.warning("Could not load insta_settings.json: %s", e)

try:
    logging.info("Logging in as %s", USERNAME)
    cl.login(USERNAME, PASSWORD)
    logging.info("Login OK")
except Exception as e:
    logging.exception("Login failed (challenge/2FA?). See GitHub Actions logs and Instagram security activity.")
    sys.exit(2)

try:
    friend_id = cl.user_id_from_username(FRIEND)
    logging.info("Found friend %s -> id %s", FRIEND, friend_id)
except Exception as e:
    logging.exception("Could not find friend username: %s", FRIEND)
    sys.exit(3)

try:
    cl.direct_send(MESSAGE, [friend_id])
    logging.info("Message sent to %s", FRIEND)
except Exception as e:
    logging.exception("Failed to send DM.")
    sys.exit(4)

# dump settings to file (so you can reuse session later if you want)
try:
    cl.dump_settings("insta_settings.json")
    logging.info("Saved session to insta_settings.json")
except Exception:
    logging.warning("Could not dump settings (not critical).")
