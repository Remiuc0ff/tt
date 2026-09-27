# пезда
__version__ = (1, 4, 8, 8)

from telethon import events
from .. import loader, utils
import asyncio

@loader.tds
class TikTokDownloader(loader.Module):
    """Скачивание TikTok-видео без водяных знаков"""
    strings = {"name": "TikTokDL"}

    async def ttcmd(self, message):
        """<ссылка> — Скачать TikTok без водяных знаков"""
        link = utils.get_args_raw(message)
        if not link:
            return await utils.answer(message, "🔗 Укажи ссылку на TikTok-видео")

        bot = "@downloader_tiktok_bot"

        # Мгновенный редакт
        await message.edit("<b><emoji document_id=5287613458777387650>😴</emoji> Загрузка видео...")

        try:
            async with message.client.conversation(bot, timeout=20) as conv:
                await conv.send_message(link)
                resp = await conv.get_response()
                await message.client.send_read_acknowledge(bot)

                if resp.media:
                    await message.edit(file=resp.media, text="")
                else:
                    await message.edit(f"❌ Бот ответил без медиа:\n{resp.text}")

        except asyncio.TimeoutError:
            await message.edit("Бот не ответил. Попробуй позже.")
