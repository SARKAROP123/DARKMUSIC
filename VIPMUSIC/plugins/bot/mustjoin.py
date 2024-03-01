
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from VIPMUSIC import app

#--------------------------

MUST_JOIN = "TG_NAME_STYLE"
#------------------------
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://telegra.ph/file/0c808e78173e0e54f544c.jpg", caption=f"๏ 𝐏𝐋𝐄𝐀𝐒𝐄 𝐉𝐎𝐈𝐍 𝐓𝐇𝐈𝐒 𝐂𝐇𝐀𝐍𝐍𝐄𝐋  [๏sᴜᴘᴘᴏʀᴛ๏]({link}) 𝐓𝐇𝐀𝐍 𝐒𝐓𝐀𝐑𝐓 𝐌𝐘 𝐌𝐔𝐒𝐈𝐂 𝐁𝐎𝐓 [๏sᴜᴘᴘᴏʀᴛ๏]({link}) 𝐉𝐎𝐈𝐍 𝐀𝐍𝐃 𝐓𝐇𝐀𝐍𝐊𝐒 𝐔𝐒𝐄𝐈𝐍𝐍𝐆 𝐌𝐘 𝐌𝐔𝐒𝐈𝐂 𝐁𝐎𝐓 ! ",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("๏𝐉𝐎𝐈𝐍๏", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"๏𝐏𝐑𝐎𝐌𝐎𝐓𝐄 𝐌𝐄 𝐀𝐒 𝐀𝐍 𝐀𝐃𝐌𝐈𝐍 𝐀𝐒 𝐓𝐇𝐄 𝐌𝐔𝐒𝐓_𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐓 ๏: {MUST_JOIN} !")
