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