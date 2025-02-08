from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

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

@app.route('/')
def home():
    return render_template('home.html')

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

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_email', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
