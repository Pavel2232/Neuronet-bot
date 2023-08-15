import logging

import vk_api as vk

from bots_logger import VkLogger
from dialogflow_api import detect_intent_text
from tg_bot import env
import random

from vk_api.longpoll import VkLongPoll, VkEventType

logger = logging.getLogger('BotVK')


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    vk_session = vk.VkApi(token=env("VK_BOT_TOKEN"))
    vk_api = vk_session.get_api()
    long_poll = VkLongPoll(vk_session)
    logger.info('Бот запущен')
    logger.addHandler(VkLogger(vk_api, env('VK_CHAT_ID')))
    while True:
        try:
            for event in long_poll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    answer = detect_intent_text(project_id=env('PROJECT_ID'), session_id=event.user_id,
                                                message_to_dialogflow=event.text)
                    if answer.query_result.intent.is_fallback:
                        continue
                    else:
                        vk_api.messages.send(
                            user_id=event.user_id,
                            message=answer.query_result.fulfillment_text,
                            random_id=random.randint(1, 1000)
                        )
        except Exception as e:
            logger.exception(e)


if __name__ == "__main__":
    main()
