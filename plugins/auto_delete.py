import pyrogram 
from pyrogram import Client, Filters 

@Client.on_message()
async def delete(c, m):
    if m.from_user is None:
       await m.delete()
