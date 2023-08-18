from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update

from environs import Env
from speech_recognition import detect_intent_texts


def main():
    env = Env()
    env.read_env()
    tg_bot_token = env('TG_BOT_TOKEN')
    tg_user_id = env('TG_USER_ID')
    google_project_id = env('GOOGLE_PROJECT_ID')

    updater = Updater(token=tg_bot_token, use_context=True)

    def start(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm an echo bot, please talk to me!")

    def echo(update: Update, context: CallbackContext):
        text = detect_intent_texts(google_project_id, tg_user_id, texts=[update.message.text], language_code='ru-RU')

        context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    start_handler = CommandHandler('start', start)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)
    updater.start_polling()


if __name__ == '__main__':
    main()
