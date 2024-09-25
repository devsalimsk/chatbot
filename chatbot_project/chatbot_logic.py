import json


# Load chatbot responses from a JSON file
def load_responses():
    with open('knowledge_base.json', 'r') as f:
        return json.load(f)


responses = load_responses()


def get_response(user_input):
    # Simple matching logic
    user_input = user_input.lower()

    for intent in responses['intents']:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input:
                return intent['responses'][0]

    # Default response if no pattern matches
    return "Sorry, I don't understand. Can you rephrase?"
