from pyrogram import filters
from aditya import adi
import asyncio
import os

from_grup=os.getenv("FROM_GROUP")
to_grup=os.getenv("TO_GROUP")

@adi.on_message(filters.chat(from_grup))
async def pm(client, message):
  await message.forward(to_grup)
