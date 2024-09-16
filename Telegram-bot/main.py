from telegram.ext import Updater
import settings

# Добавляем словарь со настройками прокси
PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080', 'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

def main():
    mybot = Updater(settings.API_key, use_context=True)
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()