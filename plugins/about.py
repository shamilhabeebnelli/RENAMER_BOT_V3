from pyrogram import Client, filters


@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	await message.reply_text("prrr")
