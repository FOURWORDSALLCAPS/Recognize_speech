import json
import argparse

from google.cloud import dialogflow
from environs import Env


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    """Create an intent of the given intent type."""

    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )


def main():
    parser = argparse.ArgumentParser(description='Данный код позволяет создать намерения на сайте Doalogflow',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--dest_file', type=str,
                        help='Путь к каталогу с тренировочными данными')
    args = parser.parse_args()
    env = Env()
    env.read_env()
    google_project_id = env('GOOGLE_PROJECT_ID')
    with open(args.dest_file, "r", encoding='UTF-8') as file:
        file_contents = file.read()

    file_content = json.loads(file_contents)

    for key, value in file_content.items():
        create_intent(
            project_id=google_project_id,
            display_name=key,
            training_phrases_parts=value['questions'],
            message_texts=value['answer']
        )


if __name__ == '__main__':
    main()
