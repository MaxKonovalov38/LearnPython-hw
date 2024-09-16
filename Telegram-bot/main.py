from telegram.ext import Updater, CommandHandler
import settings

# Добавляем словарь со настройками прокси
#PROXY = {'proxy_url': 'socks5h://t3.learn.python.ru:1080', 'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def greet_user(update, context):
    print('Вызван /start')


# Добавляем поддержку прокси (в итоге пришлось закоментировать, т.к. подключение через прокси невозможно)
def main():
    #mybot = Updater(settings.API_key, use_context=True, request_kwargs=PROXY)
    mybot = Updater(settings.API_key, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()