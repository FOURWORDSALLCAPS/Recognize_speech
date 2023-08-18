import random
import vk_api as vk

from vk_api.longpoll import VkLongPoll, VkEventType
from environs import Env
from speech_recognition import detect_intent_texts


def echo(event, vk_api, text):
    vk_api.messages.send(
        user_id=event.user_id,
        message=text,
        random_id=random.randint(1, 1000)
    )


if __name__ == "__main__":
    env = Env()
    env.read_env()
    vk_group_token = env('VK_GROUP_TOKEN')
    tg_user_id = env('TG_USER_ID')
    google_project_id = env('GOOGLE_PROJECT_ID')

    vk_session = vk.VkApi(token=vk_group_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            text = detect_intent_texts(google_project_id, tg_user_id, texts=[event.text],
                                       language_code='ru-RU')
            echo(event, vk_api, text)
