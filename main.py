from flask import Flask, jsonify, request

app = Flask(__name__)

# Load the content of the sample knowledge base into memory
with open('README.md', 'r') as file:
    info = file.read()

# In-memory storage for chat histories
chat_histories = {}

@app.route('/chat', methods=['POST'])
def chat():
    print("Received a chat request")
    print(request.json)
    # Get the user's message from the request
    data = request.json
    username = data['username']
    message = data['message']

    # TODO: Generate a response based on the user's message and the content of info.txt
    response = 'I received\n' + message

    # Add the user's message and the response to their chat history
    if username not in chat_histories:
        chat_histories[username] = []
    chat_histories[username].append({
        'username': username,
        'message': message,
        'response': response
    })

    # Return the response
    return jsonify({'response': response})

@app.route('/history', methods=['GET'])
def history():
    # Get the username from the request parameters
    username = request.args.get('username')

    # Fetch the user's chat history
    history = chat_histories.get(username, [])

    # Return the chat history
    return jsonify(history)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)  # Listening on all public IPs
