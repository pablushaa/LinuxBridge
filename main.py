from aiogram.client.default import DefaultBotProperties
from aiogram.types.callback_query import CallbackQuery
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command

import asyncio, config, utils, kb, subprocess, os

bot = Bot(token=config.TOKEN)
dp = Dispatcher()
router = Router()

class Form(StatesGroup):
    text_prompt = State()
    img_prompt = State()


async def main():
    for admin in config.ADMINS:
        await bot.send_message(admin, "✅ *Бот успешно запущен*", parse_mode=ParseMode.MARKDOWN_V2, reply_markup=kb.kb)
    await dp.start_polling(bot, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2))


@dp.message(F.text == "🏚 Главное меню")
@dp.message(Command("start"))
async def test(msg: types.Message):
    if msg.from_user.id not in config.ADMINS:
        return

    greet = utils.getGreet(msg)
    await bot.send_photo(
        msg.chat.id,
        photo=types.FSInputFile("wallpaper.jpg"),
        caption=greet,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=kb.menu
    )


@dp.message(F.text == "❔ О боте")
async def about(msg: types.Message):
    await msg.answer("👤 Создатель: *@pablusha*\n📔 GitHub: *[LinuxBridge](https://github.com/pablushaa/LinuxBridge)*", parse_mode=ParseMode.MARKDOWN_V2)


@dp.callback_query(F.data == "reboot")
async def reboot(call: CallbackQuery):
    message = await call.message.answer("*🔄 Перезагружаюсь\\.\\.\\.*", parse_mode=ParseMode.MARKDOWN_V2, reply_markup=kb.kb)
    subprocess.run(["reboot"])
    await call.answer()


@dp.callback_query(F.data == "screen")
async def screen(call: CallbackQuery):
    res = subprocess.run(["./maim", "screen.png"], capture_output=True, text=True)
    await bot.send_photo(
        call.message.chat.id,
        photo=types.FSInputFile("screen.png"),
        reply_markup=kb.kb
    )
    await call.answer()
    os.remove("screen.png")


if __name__ == "__main__":
    asyncio.run(main())