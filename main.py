from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, types

import datetime, asyncio, config, psutil, utils


bot = Bot(token=config.TOKEN)
dp = Dispatcher()

async def main():
    await dp.start_polling(bot, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2))


@dp.message(Command("start"))
async def test(msg: types.Message):
    if msg.from_user.id not in config.ADMINS:
        return

    now = datetime.datetime.now()
    disk = psutil.disk_usage("/")

    # ненавижу этот уродский маркДАУН, из-за него код с этими реплейсами тупо нечитабелен((99(
    greet = f"""
👋 Привет, *{ msg.from_user.mention_markdown(msg.from_user.full_name) }* 
🖥 Статистика хоста *{ open("/etc/hostname").read().replace("\n", "") }:*

> Процессор: *{str(psutil.cpu_percent()).replace(".", "\\.")}%*
> ОЗУ: *{str(psutil.virtual_memory().percent).replace(".", "\\.")}%*
> Диск: *{str(disk.percent).replace(".", "\\.")}%* \\| *{int(disk.used / 1024 ** 3)} из {int(disk.total / 1024 ** 3)}ГБ*
>
> Аптайм: *{str(round(float(open("/proc/uptime").read().split()[0]) / 3600, 2)).replace(".", "\\.")}* часа \\(ов\\)
    """

    utils.downloadCat() # коты это круто, но потом сделаю так, чтобы пользователь сам мог выбирать "заставку"
    await bot.send_photo(msg.chat.id, photo=types.FSInputFile("cat.jpg"), caption=greet, parse_mode=ParseMode.MARKDOWN_V2)


if __name__ == "__main__":
    asyncio.run(main())