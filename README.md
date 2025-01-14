# Flask CDP Chatbot

This project is a Flask-based chatbot that provides detailed, formatted instructions for tasks related to various Customer Data Platforms (CDPs) such as Segment, mParticle, Lytics, and Zeotap. The chatbot answers questions about setting up sources, creating user profiles, building audience segments, and integrating data with CDPs.

## Features

- **Flask Web Application**: Built with Flask to provide a backend for serving responses to user queries.
- **Question Answering**: Handles specific questions regarding CDP-related tasks (Segment, mParticle, Lytics, Zeotap).
- **Formatted Responses**: Returns answers in a readable and structured format with numbered lists and bullet points.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/RohitUJadhav/CDP_ChatBot.git
    cd cdp-chatbot
    ```

2. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

   Or manually:
    ```bash
    pip install Flask
    ```

3. Run the Flask application:
    ```bash
    python app.py
    ```

   The application will run on `http://127.0.0.1:5000/`.

## API Endpoints

### `GET /`
- Displays a welcome message: `"Welcome to the CDP Chatbot!"`

### `POST /ask`
- Accepts a JSON request body with a `question` field, which should contain the user's query.
- Returns a formatted response in JSON with the answer.

#### Request Example:
```json
{
  "question": "How can I integrate my data with Zeotap?"
}
