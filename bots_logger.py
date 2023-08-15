import logging
import random


class TelegramLogger(logging.Handler):

    def __init__(self, bot, chat_id):
        super().__init__()
        self.chat_id = chat_id
        self.tg_bot = bot

    def emit(self, record):
        log = self.format(record)
        send_message = self.tg_bot.send_message(chat_id=self.chat_id, text=log)


class VkLogger(logging.Handler):

    def __init__(self, vk_bot, chat_id):
        super().__init__()
        self.vk_bot = vk_bot
        self.chat_id = chat_id

    def emit(self, record):
        log = self.format(record)
        send_message = self.vk_bot.messages.send(
            user_id=self.chat_id,
            message=log.query_result.fulfillment_text,
            random_id=random.randint(1, 1000)
        )
