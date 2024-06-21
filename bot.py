import asyncio
import json
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

import config
from salary_aggregator.aggregator import aggregate_salaries

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer('Hello! Send me a JSON with dt_from, dt_upto, and group_type to get aggregated salary data. '
                         'Example: '
                         '{"dt_from": "2022-09-01T00:00:00", "dt_upto": "2022-12-31T23:59:00", "group_type": "month"}')


@dp.message()
async def handle_message(message: Message) -> None:
    try:
        data = json.loads(message.text)
        dt_from = data['dt_from']
        dt_upto = data['dt_upto']
        group_type = data['group_type']
        result = aggregate_salaries(dt_from, dt_upto, group_type)

        await message.reply(json.dumps(result))
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")


async def main() -> None:
    bot = Bot(token=config.TELEGRAM_API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
