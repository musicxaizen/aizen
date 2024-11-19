import random
import string
from pyrogram import Client, filters, enums
from Dev import app

def generate_strong_password(length):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+"

    # Ensure the password has at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars),
    ]

    # Fill the rest of the password length with random choices from all sets
    all_chars = lowercase + uppercase + digits + special_chars
    password += random.choices(all_chars, k=length - len(password))

    # Shuffle to prevent predictable patterns
    random.shuffle(password)
    
    # Join the list into a string
    return ''.join(password)

@app.on_message(filters.command(["genpass", 'genpw', "genpassword"]))
async def password(bot, update):
    message = await update.reply_text(text="ᴘʀᴏᴄᴇꜱꜱɪɴɢ...")
    
    if len(update.command) > 1:
        qw = update.text.split(" ", 1)[1]
    else:
        ST = ["12", "14", "16", "18", "20"]  # Stronger password length
        qw = random.choice(ST)
    
    limit = int(qw)
    random_value = generate_strong_password(limit)
    
    txt = f"<b>ʟɪᴍɪᴛ :</b> {str(limit)} \n<b> ᴘᴀꜱꜱᴡᴏʀᴅ: <code>{random_value}</code>"
    
    await message.edit_text(text=txt, parse_mode=enums.ParseMode.HTML)
