import config
from telethon import TelegramClient
#Обрабатываю простой сценарий использования, проверяю старт, перевод и вызов меню настройки языка
api_id = config.api_id
api_hash = config.api_hash
bot = "@hjkhjkbot"


async def test_start(client: TelegramClient):
    async with client.conversation(bot, timeout=10) as conv:
        await conv.send_message("/start")
        resp = await conv.get_response()

        text = "Добро пожаловать!" \
               "\n\nЯ - бот созданный переводить введеный тобой текст, на один из 16 доступный языков." \
               "\n\nВсё что от тебя нужно, выбрать язык, на который нужно перевести текст, а остальное я сделаю сам.\n" \
               "По умолчанию стоит английский язык." \
               "\n\n/lang - чтобы изменить языка"
        assert text == resp.raw_text

async def test_lang(client: TelegramClient):
    async with client.conversation(bot, timeout=5) as conv:
        await conv.send_message("/lang")
        resp = await conv.get_response()
        text = 'Выбери язык, сейчас установлен English:'
        assert text == resp.raw_text


async def test_trans(client: TelegramClient):
    async with client.conversation(bot, timeout=5) as conv:
        await conv.send_message("Привет, меня зовут тест, я тестирую бота. "
                                "Hi, my name is test, I test the bot")
        resp = await conv.get_response()
        text = 'Hi, my name is test, I test the bot. ' \
               'Hi, my name is test, I test the bot'
        assert text == resp.raw_text



with TelegramClient('kek', api_id, api_hash) as client:
    client.loop.run_until_complete(test_start(client))
    client.loop.run_until_complete(test_trans(client))
    client.loop.run_until_complete(test_lang(client))




