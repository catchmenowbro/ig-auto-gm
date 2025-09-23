# safe_send_dm.py
# Tries session login first (if session.json present), else falls back to username/password


from instagrapi import Client
import os, json, sys


TARGET_ENV = 'IG_TARGET'


cl = Client()


username = os.getenv('IG_USERNAME')
password = os.getenv('IG_PASSWORD')
target = os.getenv('IG_TARGET')
message = os.getenv('IG_MESSAGE', 'Good Morning 🌥️')


def load_session():
if os.path.exists('session.json'):
try:
data = json.load(open('session.json'))
return data.get('sessionid')
except Exception:
return None
return None


sessionid = load_session()


try:
if sessionid:
try:
cl.login_by_sessionid(sessionid)
print('Logged in by sessionid')
except Exception as e:
print('Session login failed:', e)
if username and password:
cl.login(username, password)
print('Logged in by username/password fallback')
else:
if username and password:
cl.login(username, password)
print('Logged in by username/password')


if not target:
print('IG_TARGET missing')
sys.exit(2)
