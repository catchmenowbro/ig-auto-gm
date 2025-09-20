from instagrapi import Client
import os

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

cl = Client()

try:
    # Load old session
    cl.load_settings("insta_settings.json")
    cl.login(USERNAME, PASSWORD)
except:
    # Fresh login if old session invalid
    cl.login(USERNAME, PASSWORD)

# Save updated session
cl.dump_settings("insta_settings.json")
print("Session refreshed successfully!")
