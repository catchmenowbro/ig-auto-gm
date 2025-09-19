from instagrapi import Client

cl = Client()
cl.load_settings("insta_settings.json")
cl.login_by_sessionid(cl.get_settings()["authorization_data"]["sessionid"])

user_id = cl.user_id_from_username("nidhi_username")  # yaha uska username daal
cl.direct_send("Good Morning 🌞💖", [user_id])
