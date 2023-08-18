import json

from environs import Env


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    """Create an intent of the given intent type."""
    from google.cloud import dialogflow

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

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )


def main():
    env = Env()
    env.read_env()
    google_project_id = env('GOOGLE_PROJECT_ID')
    with open("training_phrases.json", "r", encoding='UTF-8') as my_file:
        file_contents = my_file.read()

    create_intent(
        project_id=google_project_id,
        display_name='Устройство на работу',
        training_phrases_parts=json.loads(file_contents)['Устройство на работу']['questions'],
        message_texts=json.loads(file_contents)['Устройство на работу']['answer']
    )


if __name__ == '__main__':
    main()
