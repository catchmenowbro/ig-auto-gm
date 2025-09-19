from instagrapi import Client

cl = Client()

# Session restore
cl.load_settings("insta_settings.json")

try:
    sessionid = cl.get_settings()["authorization_data"]["sessionid"]
    cl.login_by_sessionid(sessionid)
    print("✅ Session restore successful")
except Exception as e:
    print("⚠️ Session restore failed:", e)
    exit(1)

# Friend username daal
friend_username = "itsp.aru01"   # yaha asli username daalna

try:
    user_id = cl.user_id_from_username(friend_username)
    cl.direct_send("Good Morning 🌞💖", [user_id])
    print("📩 Good Morning message sent successfully!")
except Exception as e:
    print("❌ Failed to send message:", e)
