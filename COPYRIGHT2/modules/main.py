from pyrogram import Client, filters
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
from config import OWNER_ID, BOT_USERNAME
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
            InlineKeyboardButton("• Oᴡɴᴇʀ •", url="https://t.me/harshu_Raven")
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

# Auto-delete Media
@app.on_message(filters.group & (filters.animation | filters.audio | filters.document | filters.photo | filters.sticker | filters.video))
async def auto_delete_media(client, message):
    await message.reply_text(
        "⚡ **Your media will be automatically deleted after 15 minutes.**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Uᴘᴅᴀᴛᴇs", url="https://t.me/Sparrow_Bots")]]
        ),
        quote=False
    )
    await asyncio.sleep(900)  # 15 minutes
    await message.delete()

# Delete Edited Messages
@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    await edited_message.reply_text(
        "⚠️ **Your edited message will be deleted after 5 minutes.**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Uᴘᴅᴀᴛᴇs", url="https://t.me/Sparrow_Bots")]]
        ),
        quote=False
    )
    await asyncio.sleep(300)  # 5 minutes
    await edited_message.delete()
