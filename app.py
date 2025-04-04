#Author: Sajeeb Chandra Das
#Student ID: 11189246

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# Database file name
DATABASE = 'chat.db'

# Function to initialize the database and create tables if not already existing
def init_db():
    if not os.path.exists(DATABASE):  # Check if the database file exists
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS chats (id INTEGER PRIMARY KEY, topic TEXT, creator TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, chat_id INTEGER, sender TEXT, content TEXT)''')
        conn.commit()
        conn.close()

# Initialize database when the app starts
init_db()

# Home route: List of chats and form to create a new chat
@app.route("/", methods=["GET", "POST"])
def home():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    if request.method == "POST":
        topic = request.form["topic"]
        creator = request.form["creator"]
        sender = request.form["sender"]
        message_content = request.form["content"]

        # Add the chat topic, creator, and first message in the new chat
        cursor.execute("INSERT INTO chats (topic, creator) VALUES (?, ?)", (topic, creator))
        chat_id = cursor.lastrowid  # Get the chat ID of the newly created chat
        cursor.execute("INSERT INTO messages (chat_id, sender, content) VALUES (?, ?, ?)", (chat_id, sender, message_content))
        conn.commit()
        return redirect(url_for("home"))

    cursor.execute("SELECT * FROM chats")
    chats = cursor.fetchall()
    conn.close()
    return render_template("home.html", chats=chats)

# Chat route to show messages and allow adding new ones
@app.route("/chat/<int:chat_id>", methods=["GET", "POST"])
def chat(chat_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    if request.method == "POST":
        sender = request.form["sender"]
        content = request.form["content"]
        cursor.execute("INSERT INTO messages (chat_id, sender, content) VALUES (?, ?, ?)", (chat_id, sender, content))
        conn.commit()

    cursor.execute("SELECT * FROM chats WHERE id=?", (chat_id,))
    chat_topic = cursor.fetchone()

    cursor.execute("SELECT sender, content FROM messages WHERE chat_id=?", (chat_id,))
    messages = cursor.fetchall()
    conn.close()
    return render_template("chat.html", chat_topic=chat_topic, messages=messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)