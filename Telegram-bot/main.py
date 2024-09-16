import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

# Записываем отчет о работе бота
logging.basicConfig(filename='bot.log', level=logging.INFO)

# Добавляем словарь со настройками прокси
#PROXY = {'proxy_url': setting.PROXY_URL,
#    'urllib3_proxy_kwargs': {
#        'username': settings.PROXY_USERNAME,
#        'password': settings.PASSWORD
#    }
#}

# Функция которая будет "отвечать" пользователю
def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


# Функция посылает на запрос ответ
def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')


# Добавляем поддержку прокси (в итоге пришлось закоментировать, т.к. подключение через прокси невозможно)
def main():
    #mybot = Updater(settings.API_key, use_context=True, request_kwargs=PROXY)
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    # Дщгирование старта бота
    logging.info("[--*--] TelegramBot -- START")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()