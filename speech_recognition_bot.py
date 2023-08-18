from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update

from environs import Env
from google.cloud import dialogflow


def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs."""

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)

    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)

        query_input = {
            "text": {
                "text": text_input.text,
                "language_code": text_input.language_code
            }
        }

        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )
        response_dialogflow = response.query_result.fulfillment_text

        return response_dialogflow


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
