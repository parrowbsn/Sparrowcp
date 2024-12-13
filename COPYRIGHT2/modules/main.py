from pyrogram import Client, filters
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message
import time
import psutil
import platform
import asyncio
import logging
from config import OWNER_ID, BOT_USERNAME
from COPYRIGHT2 import COPYRIGHT2 as app

# ----------------------------------------------------------------------------------------
# Expanded forbidden keywords
FORBIDDEN_KEYWORDS = [
    "syllabus", "textbook", "NCERT", "CBSE", "ICSE", "XII", "XI", "grade", "class", 
    "exam", "quiz", "test", "assignments", "notes", "answers", "solutions", 
    "teacher", "professor", "student", "school", "college", "education", 
    "study", "studies", "paper", "worksheet", "mock", "tutor", "online class", 
    "tuition", "math", "physics", "chemistry", "biology", "science", "history", 
    "geography", "political science", "economics", "sociology", "computer science", 
    "programming", "java", "python", "C++", "HTML", "CSS", "coding", "midterm", 
    "semester", "project", "pdf", "ppt", "word document", "docx", "lab report", 
    "practical", "experiment", "research", "dissertation", "thesis", "abstract", 
    "case study", "journal", "reference material", "SAT", "ACT", "GRE", "GMAT", 
    "TOEFL", "IELTS", "JEE", "NEET", "board exam", "finals", "prelims", 
    "entrance exam", "admission test", "study material", "previous year paper", 
    "sample paper", "model answers", "solution key", "exam guide", "cheatsheet", 
    "handouts", "reference books", "System.in", "Scanner", "void", "main", 
    "import java", "public static", "nextInt", "exception handling", "loops", 
    "arrays", "data structures", "copyright", "plagiarism", "illegal", 
    "piracy", "unauthorized", "reproduction", "duplicate content", 
    "intellectual property", "Khan Academy", "Byju's", "Unacademy", "Coursera", 
    "Udemy", "edX", "Quizlet", "Duolingo", "Skillshare", "Chegg", "Bartleby", 
    "Toppr", "Vedantu", "Extramarks", "WhiteHat Jr", "LinkedIn Learning", 
    "page", "chapter", "exercise", "solution", "practice", "formula", 
    "equation", "definition", "diagram", "graph", "table", "chart"
]

start_txt = """<b> ˹ 𝗧ᴇ𝘅ᴛ 𝗧ᴇʀᴍɪɴᴀᴛᴏʀ ˼ </b>

Wᴇʟᴄᴏᴍᴇ I ᴀᴍ ˹ 𝗧ᴇ𝘅ᴛ 𝗧ᴇʀᴍɪɴᴀᴛᴏʀ ˼ ᴡʜɪᴄʜ ᴅᴇᴛᴇᴄᴛs ᴄᴏᴘʏʀɪɢʜᴛ ᴍᴇᴛᴇʀɪᴀʟ ᴀɴᴅ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ɪᴛ Aʟᴡᴀʏs ғʀᴇᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ғʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ©️ ɪssᴜᴇs ⚡ .

⚡Hᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ :- Jᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ɢɪᴠᴇ sᴏᴍᴇ ᴘᴏᴡᴇʀs ✨"""

# ----------------------------------------------------------------------------------------

# Start Command
@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• Oᴡɴᴇʀ •", callback_data="dil_back")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/507986c81f04c68396cef-a9f06b609e411d6481.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )

# Handle Forbidden Keywords
@app.on_message()
async def handle_forbidden_keywords(client, message):
    """
    Detect forbidden keywords and delete messages after 5 minutes.
    """
    if any(keyword.lower() in (message.text or "").lower() for keyword in FORBIDDEN_KEYWORDS) or \
       any(keyword.lower() in (message.caption or "").lower() for keyword in FORBIDDEN_KEYWORDS):
        
        # Notify the user about pending deletion
        await message.reply_text(
            f"⚠️ **Your message contains educational or copyright-sensitive content. It will be deleted within 5 minutes.**",
            quote=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Uᴘᴅᴀᴛᴇs", url="https://t.me/Sparrow_Bots")]]
            )
        )
        
        # Wait 5 minutes before deleting the message
        await asyncio.sleep(300)
        await message.delete()

# Auto-delete media after 15 minutes
@app.on_message(filters.animation | filters.audio | filters.document | filters.photo | filters.sticker | filters.video)
async def auto_delete_media(client, message):
    """
    Automatically delete media files after 15 minutes.
    """
    # Add "Updates" button
    await message.reply_text(
        f"⚡ **Your media will be automatically deleted after 15 minutes.**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Uᴘᴅᴀᴛᴇs", url="https://t.me/Sparrow_Bots")]]
        ),
        quote=False
    )
    await asyncio.sleep(900)  # Wait for 15 minutes
    await message.delete()

# Delete Edited Messages
@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    """
    Delete edited messages after 5 minutes.
    """
    username = edited_message.from_user.username if edited_message.from_user else "Unknown User"
    await edited_message.reply_text(
        f"⚠️ **Your edited message will be deleted after 5 minutes.**",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Uᴘᴅᴀᴛᴇs", url="https://t.me/Sparrow_Bots")]]
        ),
        quote=False
    )
    await asyncio.sleep(300)  # Wait 5 minutes
    await edited_message.delete()
