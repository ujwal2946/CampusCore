import sqlite3
import os

# Get the directory where add_user.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'database.db')

# Connect to the database
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# Check if user exists
c.execute("SELECT * FROM users WHERE username = 'track'")
user = c.fetchone()

if user:
    print(f"User 'track' already exists: {user}")
else:
    # Create the attendance staff user
    c.execute("INSERT INTO users (username, password, role) VALUES ('track', '2946', 'attendance')")
    conn.commit()
    print("User 'track' created successfully!")

# Verify the user was created
c.execute("SELECT * FROM users WHERE username = 'track'")
user = c.fetchone()
if user:
    print(f"User details: {user}")

conn.close()
