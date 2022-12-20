import asyncio

from aiogram import Bot, Dispatcher, types, html
from aiogram.filters import Command, CommandObject

dp = Dispatcher()
TOKEN = '5635868122:AAE2eEa9g0lMiJRiYF5bDO88UxQP4XH7fmI'
bot = Bot(TOKEN)


async def main():
    await dp.start_polling(bot)


@dp.message(Command(commands=["members"]))
async def cmd_members(message: types.Message):
    cnt = await bot.get_chat_members_count(chat_id=message.chat.id)
    await message.answer(f"In your chat there are {cnt} people.")


@dp.message(Command(commands=["admins"]))
async def cmd_admins(message: types.Message):
    admins = await bot.get_chat_administrators(message.chat.id)
    admins_full_name = []
    for admin in admins:
        admins_full_name.append(admin.user.full_name)
    await message.answer(f"Admins in this chat {', '.join(admins_full_name)}")


@dp.message(Command(commands=["leave"]))
async def cmd_leave(message: types.Message):
    await message.answer("Goodbye!")
    await bot.leave_chat(message.chat.id)


@dp.message(Command(commands=["bold"]))
async def cmd_bold(message: types.Message, command: CommandObject):
    await message.answer(f"{html.bold(html.quote(command.args))}", parse_mode="HTML")


@dp.message(Command(commands=["time"]))
async def cmd_time(message: types.Message):
    import datetime
    await message.answer(f"Now is: <b>{datetime.datetime.now().strftime('%H:%M')}</b>", parse_mode="HTML")


@dp.message(Command(commands=["start"]))
async def cmd_start(message: types.Message):
    await message.answer(f"You have started bot! Write /help to check commands")


@dp.message(Command(commands=["help"]))
async def cmd_help(message: types.Message):
    await message.answer(
        "Available commands:\n"
        "\\time -- to get time\n"
        "\\bold {text} -- to make your {text} bold\n"
        "\\leave -- to make bot leave chat\n"
        "\\admins -- to get all chat admins\n"
        "\\members -- to get all chat members\n"
        "\\help -- to get all commands\n"
        "\\start -- to start bot\n"
    )


if __name__ == '__main__':
    asyncio.run(main())
