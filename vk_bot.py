import logging
import vk_api as vk
from environs import Env
from bots_logger import VkLogger
from dialogflow_api import detect_intent_text
import random
from vk_api.longpoll import VkLongPoll, VkEventType

logger = logging.getLogger('BotVK')


def main(vk_bot_token: str, vk_chat_id: int):
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    vk_session = vk.VkApi(token=vk_bot_token)
    vk_api = vk_session.get_api()
    long_poll = VkLongPoll(vk_session)
    logger.info('Бот запущен')
    logger.addHandler(VkLogger(vk_api, vk_chat_id))
    while True:
        try:
            for event in long_poll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    answer = detect_intent_text(project_id=env('PROJECT_ID'), session_id=event.user_id,
                                                message_to_dialogflow=event.text)
                    if not answer.query_result.intent.is_fallback:
                        vk_api.messages.send(
                            user_id=event.user_id,
                            message=answer.query_result.fulfillment_text,
                            random_id=random.randint(1, 1000)
                        )
        except Exception as error:
            logger.exception(error)

if __name__ == "__main__":
    env = Env()
    env.read_env('.env')

    vk_bot_token = env("VK_BOT_TOKEN")
    vk_chat_id = env('VK_CHAT_ID')

    main(vk_bot_token, vk_chat_id)
