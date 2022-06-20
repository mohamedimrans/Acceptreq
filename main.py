from pyrogram import Client, filters
from os import environ

app = Client("AutoForwarder", api_id=int(environ["API_ID"]), api_hash=environ["API_HASH"],
             phone_number=environ["PHONE_NUMBER"],
             session_string=environ["SESSION_STRING"]
             )

@app.on_message(filters.regex(".start") & filters.me)
async def start(app, msg):
    await msg.reply("<b>Hello I'm A Auto Join Request Accept Bot\n\nMade In India :)</b>")

@app.on_message(filters.regex(".run") & filters.me)
async def run(app, msg):
    await msg.reply("<b>Accepting All Requests...</b>")
    X = "acceser"
    get = await app.get_messages(chat_id=X, message_ids=3)
    getint = int(get.text)
    while get.text != "none":
        get = await app.get_messages(chat_id=X, message_ids=3)
        await app.approve_all_chat_join_requests(getint)
        if get.text == "none":
            break        

print("Bot Is Alive..")
app.run()
