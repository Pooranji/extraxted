from pyrogram import Client, filters
from pyrogram.types import Message
import os
import sys

# Initialize the bot with a name or API configuration
app = Client("Adv_sameebot")  # Replace "my_bot" with your bot's name or ID

@app.on_message(filters.command("start"))
async def start_handler(client: Client, message: Message):
    photo_url = "https://telegra.ph/file/cef3ef6ee69126c23bfe3.jpg"
    caption = (
        "**Hi, I am All in One Extractor Bot**.\n"
        "Press **/pw** for **Physics Wallah**..\n\n"
        "Press **/e1** for **E1 Coaching App**..\n\n"
        "Press **/vidya** for **Vidya Bihar App**..\n\n"
        "Press **/ocean** for **Ocean Gurukul App**..\n\n"
        "Press **/winners** for **The Winners Institute**..\n\n"
        "Press **/rgvikramjeet** for **Rgvikramjeet App**..\n\n"
        "Press **/txt** for **Ankit With Rojgar,**\n**The Mission Institute,**\n**The Last Exam App**..\n\n"
        "Press **/cp** for **classplus app**..\n\n"
        "Press **/cw** for **careerwill app**..\n\n"
        "Press **/khan** for **Khan Gs app**..\n\n"
        "Press **/exampur** for **Exampur app**..\n\n"
        "Press **/samyak** for **Samayak Ias**..\n\n"
        "Press **/chandra** for **Chandra app**..\n\n"
        "Press **/mgconcept** for **Mgconcept app**..\n\n"
        "Press **/down** for **For Downloading Url lists**..\n\n"
        "Press **/forward** to **Forward from One channel to others**..\n\n"
        "**𝗕𝗼𝘁 𝗢𝘄𝗻𝗲𝗿: 𝒞𝓇𝓎𝓅𝓉💞𝓈𝓉𝒶𝓇𝓀**"
    )
    await client.send_photo(message.chat.id, photo=photo_url, caption=caption)

@app.on_message(filters.command("restart"))
async def restart_handler(client: Client, message: Message):
    await message.reply_text("Restarting!", quote=True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@app.on_message(filters.command("log"))
async def log_handler(client: Client, message: Message):
    log_file_path = "log.txt"
    if os.path.exists(log_file_path):
        await client.send_document(message.chat.id, log_file_path)
    else:
        await message.reply_text("Log file not found.")

@app.on_edited_message(filters.command("start"))
async def start_edited_handler(client: Client, message: Message):
    # Handling edited /start commands if needed
    await start_handler(client, message)  # Reusing the start_handler logic for edited messages

@app.on_edited_message(filters.command("restart"))
async def restart_edited_handler(client: Client, message: Message):
    # Handling edited /restart commands if needed
    await restart_handler(client, message)  # Reusing the restart_handler logic for edited messages

@app.on_edited_message(filters.command("log"))
async def log_edited_handler(client: Client, message: Message):
    # Handling edited /log commands if needed
    await log_handler(client, message)  # Reusing the log_handler logic for edited messages

# Run the bot
app.run()
