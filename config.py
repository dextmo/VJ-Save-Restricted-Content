import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("21727017", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("8c9ff17d8d1f6fbe228e5133b011fa99", "")

#Database 
DB_URI = os.environ.get("mongodb+srv://alihaudff:111@cluster0.wqfkesd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "")
