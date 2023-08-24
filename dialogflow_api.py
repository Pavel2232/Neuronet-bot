import logging

import requests
from environs import Env
from google.cloud import dialogflow

logger = logging.getLogger('BotTG')

def detect_intent_text(project_id, session_id, message_to_dialogflow, language_code='ru'):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=message_to_dialogflow, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    return response


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    """Create an intent of the given intent type."""
    from google.cloud import dialogflow

    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=[message_texts])
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    print("Intent created: {}".format(response))


def fill_intent(link: str, project_id: str):
    try:
        response = requests.get(link)
        question_answer = response.json()
        for question_title, question in question_answer.items():
            training_phrases_parts = question.get('questions')
            answer = question.get('answer')
            create_intent(project_id, question_title, training_phrases_parts, answer)
    except Exception as error:
        logger.exception(error)


if __name__ == '__main__':
    env = Env()
    env.read_env('.env')
    fill_intent(env('DOWNLOAD_LINK'), env('PROJECT_ID'))

