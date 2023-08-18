# Бот-поддержки обученный нейросетью DialogFlow!
Бот-поддержки. 
Он будет закрывать все типичные вопросы, а вот что-то посложнее – перенаправлять на операторов.
По предварительной оценке, это на 70% сократит время ожидания ответа и на 90% повысит довольство жизнью сотрудников службы поддержки.
Специфика в том, что клиенты – люди творческие. Никогда не знаешь, как им придёт в голову сформулировать вопрос.
Предсказать варианты заранее невозможно. Поэтому бот обучаемый нейросетью! 


![Пример работы](https://github.com/Pavel2232/Neuronet-bot/blob/master/demo_tg_bot.gif)
# [Бот Тг](https://t.me/neuronet_pablo_bot)
![](https://github.com/Pavel2232/Neuronet-bot/blob/master/demo_vk_bot.gif)
# [Бот Вк](https://vk.com/club222012081)
### Как запустить проект.
1. ``` git clone https://github.com/Pavel2232/Neuronet-bot```

# [Получить апи ключи гугл](https://cloud.google.com/docs/authentication/provide-credentials-adc#how-to)

2. Установите необходимые библиотеки  ```poetry install```

3. Создайте файл .env и заполните следующие значения:
* TG_BOT_KEY=ключ телеграм бота 
* VK_BOT_TOKEN=ключ вк бота 
* DIALOGFLOW_API_KEY=API токен DIALOGFLOW
* PROJECT_ID=PROJECT_ID от DIALOGFLOW
* VK_CHAT_ID=ваш чат айди
* TG_CHAT_ID= ваш чат айди(Чтобы получить свой chat_id, напишите в Telegram специальному боту: @userinfobot)


4. Для запуска программы:
```python tg_bot.py```
```python vk_bot.py```
