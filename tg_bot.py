import logging

from environs import Env

from bots_logger import TelegramLogger
from dialogflow_api import detect_intent_text
from aiogram.types import Message
from aiogram import Dispatcher, executor, Bot

logger = logging.getLogger('BotTG')


async def conduct_dialogue(message: Message):
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger.addHandler(TelegramLogger(dp, env('TG_CHAT_ID')))
    try:
        answer = detect_intent_text(project_id=env('PROJECT_ID'), session_id=message.from_user.id,
                                    message_to_dialogflow=message.text)
        await message.answer(answer.query_result.fulfillment_text)
    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    env = Env()
    env.read_env('.env')

    bot = Bot(env('TG_BOT_KEY'))
    dp = Dispatcher(bot)

    dp.register_message_handler(conduct_dialogue)

    executor.start_polling(dp)
