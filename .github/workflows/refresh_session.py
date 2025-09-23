# refresh_session.py
# Logs in using instagrapi and writes session.json


from instagrapi import Client
import os, json, sys


username = os.getenv('IG_USERNAME')
password = os.getenv('IG_PASSWORD')


if not username or not password:
print('IG_USERNAME or IG_PASSWORD missing in env')
sys.exit(1)


cl = Client()


try:
cl.login(username, password)
# Try to get sessionid (instagrapi exposes sessionid on client in many versions)
sessionid = getattr(cl, 'sessionid', None)


data = {}
if sessionid:
data['sessionid'] = sessionid


# Also save settings (if available) — helpful for some instagrapi versions
try:
settings = cl.get_settings()
data['settings'] = settings
except Exception:
pass


# Fallback: try to export cookies to help restore session later
try:
cookies = cl.private.cookies.get_dict()
data['cookies'] = cookies
except Exception:
pass


with open('session.json', 'w') as f:
json.dump(data, f)


print('Wrote session.json (encrypted by workflow)')


except Exception as e:
print('Error refreshing session:', e)
sys.exit(2)
