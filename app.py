from flask import Flask, render_template, request, redirect, url_for, session, jsonify
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

# Login Route
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
            return "Invalid credentials!"
    
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

# Logout Route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_email', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
