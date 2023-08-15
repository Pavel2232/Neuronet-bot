import logging

from bots_logger import TelegramLogger
from dialogflow_api import detect_intent_text
from aiogram.types import Message
from environs import Env
from aiogram import Dispatcher, executor, Bot

env = Env()

env.read_env('.env')

logger = logging.getLogger('BotTG')


bot = Bot(env('TG_BOT_KEY'))
dp = Dispatcher(bot)


@dp.message_handler()
async def to_begin(message: Message):
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger.addHandler(TelegramLogger(dp, env('TG_CHAT_ID')))
    while True:
        try:
            answer = detect_intent_text(project_id=env('PROJECT_ID'), session_id=message.from_user.id,
                                    message_to_dialogflow=message.text)
            await message.answer(answer.query_result.fulfillment_text)
        except Exception as e:
            logger.exception(e)

if __name__ == '__main__':
    executor.start_polling(dp)
