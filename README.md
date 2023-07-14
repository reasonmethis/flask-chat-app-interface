# Flask Chatbot App Interface

A RESTful API for a chatbot application built with Python and Flask. The API has two primary endpoints: one for chat interaction and one for retrieving chat history. This interface can be supplement with your specific chatbot business logic.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)

## Features

- RESTful API endpoints for chatbot interaction and chat history retrieval.
- Uses Flask's built-in server for development.
- Production-grade server via Waitress for Windows environments.
- Chat history stored in-memory, by user, for the duration of the session.

## Installation

Clone this repository, then create a virtual environment, and activate it. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To start the server (Windows):

```bash
waitress-serve --listen=0.0.0.0:8000 main:app
```

## Testing

You can test the API using a tool like [Postman](https://www.postman.com/) or [curl](https://curl.se/). Alternatively, you can use the script `test.py` to send a chat message and print the response.

To send a chat message:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username":"user1", "message":"hello"}' http://localhost:8000/chat
```

To get chat history:

```bash
curl http://localhost:8000/history?username=user1
```

Replace `localhost:8000` with your server's IP address and port if you're testing from a different machine. Note that you will likely need to set up port forwarding on your router to access the server from outside your local network.

