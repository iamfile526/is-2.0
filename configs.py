# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "25841231"))
	API_HASH = os.environ.get("0a78fdfe60a7eae835d339f926f3d6a1")
	BOT_TOKEN = os.environ.get("7966453329:AAFvhQC18tsSm5eruZEeBz0Hm3MnmAsLPvc")
	BOT_USERNAME = os.environ.get("isfilestore2_bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002274560727"))
	SHORTLINK_URL = os.environ.get('linkcents.com')
	SHORTLINK_API = os.environ.get('98e5a16ac2c06520df6f8798e71b5a46b505564c')
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "7893911398"))
	DATABASE_URL = os.environ.get("mongodb+srv://hbesta123:mhfecWc6Z5wsMkTH@cluster0.ztap6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002492775782")
	LOG_CHANNEL = os.environ.get("-1002667823708", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = [int(id) for id in os.environ.get("OTHER_USERS_CAN_SAVE_FILE", "").split(",") if id.strip()]
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **My Name:** [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 **Language:** [Python 3](https://www.python.org)
│
├🔹 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹 **Hosted On:** [Heroku](https://heroku.com)
│
├🔸 **Developer:** [Predator HackerzZ](https://t.me/OwnYourBotz) 
│
├🔹 **Bot Support:** [Support Group](https://t.me/TeleRoid14)
│
├🔸 **Bot Updates:** [Bots Channel](https://t.me/TeleRoidGroup)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [@PredatorHackerzZ](https://github.com/PredatorHackerzZ)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/DonateXrobot) or ```teleroidgroup@axl```
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.

❌ **PORNOGRAPHY CONTENTS** are strictly prohibited & get Permanent Ban.
"""
