from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import google.generativeai as genai

# Initialize Flask
app = Flask(__name__)
app.secret_key = 'your_secret_key'
CORS(app)

# Configure Gemini AI
genai.configure(api_key="AIzaSyBY-_MlcCJaJpN-BPWCV25IhRaPeTYPJuE")  # Replace with your actual API key

# Database setup
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL)''')
    
    # Create notes table
    cursor.execute('''CREATE TABLE IF NOT EXISTS notes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        note TEXT,
                        FOREIGN KEY (user_id) REFERENCES users (id))''')
    
    conn.commit()
    conn.close()

init_db()

# Home Route
@app.route('/')
def home():
    return render_template('home.html')

# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, hashed_password))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            return "Email already registered!"

    return render_template('register.html')

# Updated Login Route with Flash Message
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        conn.close()
        
        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]  # Store user ID in session
            session['user_email'] = user[1]
            return redirect(url_for('dashboard'))
        else:
            flash("Oops! Wrong Password.")  # Flash message for wrong password
            return redirect(url_for('login'))
    
    return render_template('login.html')

# Dashboard Route
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        note = request.form['note']
        cursor.execute("INSERT INTO notes (user_id, note) VALUES (?, ?)", (session['user_id'], note))
        conn.commit()

    # Fetch user notes
    cursor.execute("SELECT note FROM notes WHERE user_id = ?", (session['user_id'],))
    notes = cursor.fetchall()
    conn.close()

    return render_template('dashboard.html', user=session['user_email'], notes=notes)

# AI Chatbot Route
@app.route('/chatbot')
def chatbot():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('chatbot.html')

# AI Chatbot API
@app.route('/solve_doubt', methods=['POST'])
def solve_doubt():
    try:
        data = request.get_json()
        question = data.get("question", "")

        if not question:
            return jsonify({"error": "No question provided"}), 400

        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(question)

        if not response or not response.text:
            return jsonify({"error": "AI failed to generate an answer."}), 500

        ai_answer = response.text.replace("*", "").replace(".", ".\n")

        return jsonify({"answer": ai_answer.strip()})  

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/flashcards')
def flashcards():
    return render_template("flashcards.html")

@app.route('/generate_flashcards', methods=['POST'])
def generate_flashcards():
    try:
        data = request.get_json()
        topic = data.get("topic", "")

        if not topic:
            return jsonify({"error": "No topic provided"}), 400

        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(f"Generate 5 key learning points as flashcards for the topic: {topic}")

        if not response or not response.text:
            return jsonify({"error": "AI could not generate flashcards."}), 500

        flashcards = response.text.strip().split("\n")  # Split into individual points
        return jsonify({"flashcards": flashcards})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/sticky_notes')
def sticky_notes():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, note FROM notes WHERE user_id = ?", (session['user_id'],))
    notes = cursor.fetchall()
    conn.close()

    return render_template("sticky_notes.html", notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 403

    data = request.get_json()
    note_text = data.get("note", "").strip()

    if not note_text:
        return jsonify({"error": "Note cannot be empty"}), 400

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (user_id, note) VALUES (?, ?)", (session['user_id'], note_text))
    conn.commit()
    note_id = cursor.lastrowid
    conn.close()

    return jsonify({"id": note_id, "note": note_text})

@app.route('/delete_note/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 403

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id = ? AND user_id = ?", (note_id, session['user_id']))
    conn.commit()
    conn.close()

    return jsonify({"success": True})

# Logout Route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_email', None)
    return redirect(url_for('home'))

@app.route("/todo")
def todo():
    return render_template("todo.html")


if __name__ == '__main__':
    app.run(debug=True)
