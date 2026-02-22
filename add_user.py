import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')
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
