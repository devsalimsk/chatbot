import json
from flask import Flask, request, jsonify
import chatbot_logic
from chatbot import ChatBot

app = Flask(__name__)
learning_chatbot = ChatBot(knowledge_base_file='knowledge_base.json')
chat_history = []

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'Message is required'}), 400

    # You can switch between rule-based or learning chatbot here
    use_learning_chatbot = request.json.get('use_learning_chatbot', False)

    if use_learning_chatbot:
        response = learning_chatbot.learn_and_respond(user_input)
    else:
        response = chatbot_logic.get_response(user_input)

    # Store the user input and response in chat history
    chat_history.append({'user': user_input, 'response': response})

    return jsonify({'response': response})
# Load the knowledge base (chat history) from the JSON file
with open('knowledge_base.json', 'r') as file:
    chat_history = json.load(file)

@app.route('/history', methods=['GET'])
def get_chat_history():
    return jsonify({'history': chat_history})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
