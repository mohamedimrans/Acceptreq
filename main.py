from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant

app = Client(
    "AnimeBot",
    api_id= int(environ["API_ID"]),
    api_hash= environ["API_HASH"],
    bot_token="5366663363:AAH12kmZoz9bGQoUGm8lH6qiWKhtRZ8Gt-Q"
)

force_channel = "ANIME_WORLDFORU"
force_msg_but = [[InlineKeyboardButton("CHANNEL", url="https://t.me/yazhi_ORG")]]
force_message = "<b>You Must Subscribe Our Channel To Use This Bot</b>"

send = "rmjsoa"

str_but = [

        [InlineKeyboardButton("ANIME WORLD", url="https://t.me/ANIME_WORLDFORU"),
         InlineKeyboardButton("ANIME MOVIES", url="https://t.me/ANIMEWORLD_MOVIES")],
        [InlineKeyboardButton("REQUEST/SUPPORT", url="https://t.me/ANIMEWORLDROBOT")],
        [InlineKeyboardButton("MANGA", url="https://t.me/ANIMEWORLD_MANGA"),
         InlineKeyboardButton("ANIME CHAT", url="https://t.me/ANIMEWORLD_ANIMCHAT")]
]

start5 = [[InlineKeyboardButton("ANIME CHAT", url="https://t.me/ANIMEWORLD_ANIMCHAT")]]

@app.on_message(filters.command("start") & filters.private)
async def start(app, msg):
    if force_channel:
        try:
            user = await app.get_chat_member(force_channel, msg.from_user.id)
            if user.status:
                replyi = InlineKeyboardMarkup(start5)
                text1 = "<b>Hello, Welcome To ANIME WORLD'S Bot\n\n1. You Can Request Here ❤\n\n2. You Can Clarify Your Querys ❤\n\n</b>"
                await msg.reply_text(text=text1, reply_markup=replyi)

        except UserNotParticipant:
            text = force_message
            reply_markup = InlineKeyboardMarkup(force_msg_but)
            await msg.reply_text(text=text, reply_markup=reply_markup)

@app.on_message(filters.text & filters.private)
async def echo(app, message):
    if message.from_user.id in [1225270851, 1153912202]:
        if message.text != ".run":
            replymark = InlineKeyboardMarkup(str_but)
            await message.reply(text=message.text, reply_markup=replymark)
        else:
            if message.from_user.id in [1225270851, 1153912202]:
                gette = await app.get_messages(send, 9)
                caption = await app.get_messages(send, 11)
                replymark = InlineKeyboardMarkup(str_but)
                await app.send_photo(message.chat.id, gette.text, caption=caption.text, reply_markup=replymark)

@app.on_message(filters.photo & filters.private)
async def file(app, msg):
    if msg.from_user.id in [1225270851, 1153912202]:
        await msg.reply(msg.photo.file_id)

print("OK, I'M ALIVE")
app.run()
