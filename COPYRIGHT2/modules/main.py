from pyrogram import Client, filters
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import BOT_USERNAME
from COPYRIGHT2 import COPYRIGHT2 as app

# Expanded forbidden keywords
FORBIDDEN_KEYWORDS = [
    "syllabus", "textbook", "NCERT", "CBSE", "ICSE", "grade", "class", "exam",
    "quiz", "test", "assignments", "notes", "answers", "solutions", "teacher",
    "professor", "student", "school", "college", "education", "study",
    "studies", "paper", "worksheet", "mock", "tutor", "online class", "tuition",
    "math", "physics", "chemistry", "biology", "science", "history", "geography",
    "political science", "economics", "sociology", "computer science", "copyright",
    "plagiarism", "illegal", "piracy", "unauthorized", "reproduction", "duplicate content"
]

start_txt = """<b> ˹ 𝗧ᴇ𝘅ᴛ 𝗧ᴇʀᴍɪɴᴀᴛᴏʀ ˼ </b>

Wᴇʟᴄᴏᴍᴇ I ᴀᴍ ˹ 𝗧ᴇ𝘅ᴛ 𝗧ᴇʀᴍɪɴᴀᴛᴏʀ ˼ ᴡʜɪᴄʜ ᴅᴇᴛᴇᴄᴛs ᴄᴏᴘʏʀɪɢʜᴛ ᴍᴀᴛᴇʀɪᴀʟ ᴀɴᴅ ᴀᴜᴛᴏᴅᴇʟᴇᴛᴇs ɪᴛ.⚡

⚡ **Hᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ:** Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ɢɪᴠᴇ ᴍᴏᴅᴇʀᴀᴛᴏʀ ʀɪɢʜᴛs ✨"""

# ----------------------------------------------------------------------------------------

# Start Command
@app.on_message(filters.command("start") & filters.private)
async def start(_, msg):
    buttons = [
        [InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [
            InlineKeyboardButton("Uᴘᴅᴀᴛᴇs", url="https://t.me/Sparrow_Bots"),
            InlineKeyboardButton("• Oᴡɴᴇʀ •", url="https://t.me/Sparrow_Bots")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await msg.reply_photo(
        photo="https://graph.org/file/507986c81f04c68396cef-a9f06b609e411d6481.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )

# Handle Forbidden Keywords (Silent Deletion)
@app.on_message(filters.group & ~filters.service)
async def handle_forbidden_keywords(client, message):
    if any(keyword.lower() in (message.text or "").lower() for keyword in FORBIDDEN_KEYWORDS) or \
       any(keyword.lower() in (message.caption or "").lower() for keyword in FORBIDDEN_KEYWORDS):
        await message.delete()  # Silently delete the message

# Notify and Delete Media (Audio, Photos, Videos, Documents)
@app.on_message(filters.group & (filters.audio | filters.photo | filters.video | filters.document))
async def notify_and_delete_media(client, message):
    user_mention = message.from_user.mention if message.from_user else "User"
    await message.reply_text(
        f"⚡ **{user_mention}, your media will be automatically deleted after 15 minutes.**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Uᴘᴅᴀᴛᴇs", url="https://t.me/Sparrow_Bots")]]
        ),
        quote=True
    )
    await asyncio.sleep(900)  # Wait 15 minutes
    await message.delete()

# Silently Delete Stickers and GIFs
@app.on_message(filters.group & (filters.sticker | filters.animation))
async def silent_delete_stickers_gifs(client, message):
    await asyncio.sleep(600)  # Wait 10 minutes
    await message.delete()

# Delete Edited Messages
@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    user_mention = edited_message.from_user.mention if edited_message.from_user else "User"
    await edited_message.reply_text(
        f"⚠️ **{user_mention}, your edited message will be deleted after 5 minutes.**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Uᴘᴅᴀᴛᴇs", url="https://t.me/Sparrow_Bots")]]
        ),
        quote=False
    )
    await asyncio.sleep(300)  # Wait 5 minutes
    await edited_message.delete()
