import requests

# Define the URL of your chatbot API. 
IP = "localhost" # Change this to your IP address for external access
url = f"http://{IP}:8000/chat"

# Define the message to send
data = {
    "username": "user1",
    "message": "hello"
}

# Send a POST request to the chatbot API
response = requests.post(url, json=data)

# Print the response from the server
if response.status_code == 200:
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}")
