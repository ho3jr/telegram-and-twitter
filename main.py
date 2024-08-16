from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton 
import pyromod

api_id = 18790467
api_hash = "68bf0527a74571a8dbb9cfffe70ef964"
token = "5671269812:AAGEN3LqRU4oQ8Zg1-hrSjQUDpyBJwQhq20"

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=token
)

yes_or_no = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("آره", callback_data="yes"),
         InlineKeyboardButton("نه", callback_data="no")]
    ]
)


@app.on_message(filters.channel)
async def recive_msg_channel(c: Client, m: Message):
    if m.chat.id == -1002193502389:
        if m.media:
            await app.copy_message(int("5406865643"),int(m.chat.id), m.id , caption=m.caption+"\n\n----------------\n"+"میخوای توییتش کنم؟",reply_markup=yes_or_no)
        else:
            await app.copy_message(int("5406865643"),int(m.chat.id), m.id )
            await app.send_message(int("5406865643"),"میخوای توییتش کنم؟", reply_markup= yes_or_no)

@app.on_callback_query()
async def recive_query(Client, call1):
    data = call1.data

    if data == "yes":
        pass

    elif data =="no":
        pass
    

app.run()