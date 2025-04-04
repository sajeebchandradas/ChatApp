# ChatApp

A simple web-based chat application built with Flask, SQLite, and HTML/CSS. This app allows users to create chat topics, send messages within those chats, and view them in a table format. It runs locally on port 8080 and uses SQLite for persistent storage.

## Features
- Create new chat topics with an initial message.
- Add messages to existing chats.
- View all messages in a chat in a tabular layout.
- Simple, clean UI with styled buttons and links.

## Prerequisites
- Python 3.x installed on your system.
- Git installed to clone the repository.

## Setup Instructions
1. **Clone the Repository**  
   Clone this repository to your local machine:
   ```bash
   git clone https://gitlab.com/<your-username>/chatapp.git
   cd chatapp

2. **Install Dependencies**
   Install the required Python package (Flask)
   ```bash
   pip install flask

3. **Directory Structure**
   Ensure your project directory is structured as follows:
    ```bash
   chatapp/
├── static/
│   └── style.css
├── templates/
│   ├── chat.html
│   └── home.html
├── app.py
└── README.md

4. **Run the Application**
   Start the Flask server
   ```bash
   python app.py

## Usage
1. Home Page (http://localhost:8080/)
- Enter a chat topic, your name, and a first message in the form.
- Click "Create Chat" to add a new chat.
- See the list of available chats below the form and click a topic to view its messages.

2. Chat Page (http://localhost:8080/chat/<chat_id>)
- View all messages in a table with sender and content columns.
- Add a new message by entering your name and message, then clicking "Send".
- Click "Back to Home" to return to the home page.

## File Structure
- app.py: The Flask backend that handles routing, database setup (SQLite), and chat/message management.
- templates/chat.html: HTML template for the chat page, displaying messages and a form to add new ones.
- templates/home.html: HTML template for the home page, with a form to create chats and a list of chat links.
- static/style.css: CSS file for styling the app, including buttons, tables, and links.

## Database
- The app uses SQLite with a file named chat.db, created automatically in the project root when you first run the app.
- Two tables are created:
  - chats: Stores chat topics with an id and topic.
  - messages: Stores messages with an id, chat_id, sender, and content.

## Notes
- The database file (chat.db) is not tracked in the repository. It will be generated locally when you run the app.
- To start fresh, delete chat.db and rerun app.py.

## Author
- Name: Sajeeb Chandra Das
- Student ID: 11189246
- GitLab: https://gitlab.nt.fh-koeln.de/gitlab/sadas

## License
This project is for educational purposes and not licensed for commercial use.

   

