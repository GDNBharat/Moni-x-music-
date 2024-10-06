from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Dfschinnamusic import app


start_txt = """
✦ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ !

̶꯭꯭⎯̶꯭̽❝꯭꯭💗꯭꯭꯭꯭᭄꯭꯭꯭🇹‌𝗵𝗮𝗻𝘂🇽‌𝗺𝘂𝘀𝗶𝗰🤍꯭᪳𝆺̶꯭𝅥⎯̶̶꯭̽

❅ ɪғ ʏᴏᴜ ᴡᴀɴᴛ 🇹‌𝗵𝗮𝗻𝘂 ʙᴏᴛ ʀᴇᴘᴏ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ support.
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("owner", url="https://t.me/BTSChinna_op"),
          InlineKeyboardButton("repo", url="https://github.com/dattudd/Anonxmusic-"),
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/a950dba51f34f48ddbf51.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
