from telegram.ext import Updater
import settings

def main():
    mybot = Updater(settings.API_key, use_context=True)
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()