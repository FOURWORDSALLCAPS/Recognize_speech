from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update

from environs import Env
from speech_recognition import detect_intent_texts


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm an echo bot, please talk to me!")


def reply_user(update: Update, context: CallbackContext, google_project_id, tg_user_id):
    response = detect_intent_texts(google_project_id, tg_user_id, text=update.message.text, language_code='ru-RU')

    context.bot.send_message(chat_id=update.effective_chat.id, text=response.query_result.fulfillment_text)


def main():
    env = Env()
    env.read_env()
    tg_bot_token = env('TG_BOT_TOKEN')
    tg_user_id = env('TG_USER_ID')
    google_project_id = env('GOOGLE_PROJECT_ID')

    updater = Updater(token=tg_bot_token, use_context=True)

    reply_user_handler = MessageHandler(Filters.text & (~Filters.command), lambda update, context: reply_user(
        update, context, google_project_id, tg_user_id
    ))
    start_handler = CommandHandler('start', start)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(reply_user_handler)
    updater.start_polling()


if __name__ == '__main__':
    main()
