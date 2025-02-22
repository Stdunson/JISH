import sqlite3
import re
import bcrypt
import os
from UserProfile import create_userprofile_table, profile_exists, collect_profile_data, display_user_info  # Import functions from UserProfile.py

"""
Recommendation System

Functions:
1. hash_pw(pw) - Hashes a password using bcrypt.
2. validate_pw(pw) - Validates the password against security requirements.
3. register_user(username, pw) - Registers a new user with a hashed password.
4. verify_user(username, pw) - Verifies a user's login credentials.
5. cleartable() - Clears all records from the userlogin table. Only for debugging
"""

# creating user login table
DATABASE_PATH = os.getenv('DATABASE_PATH', 'userlogin.db')
con = sqlite3.connect(DATABASE_PATH)
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS userlogin
            (username text PRIMARY KEY,
            password text)''')

# Ensure the userprofile table is created
create_userprofile_table(con)

def hash_pw(pw: str) -> str:
    # Hash password with bcrypt, the default rounds are fine for most use cases
    hashed = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')  # Decode the hashed password to a string

def validate_pw(pw):
    checks = [
        (len(pw) >= 8, "Password must be at least 8 characters long."),
        (re.search(r'[A-Z]', pw), "Password must contain at least one uppercase letter."),
        (re.search(r'[a-z]', pw), "Password must contain at least one lowercase letter."),
        (re.search(r'\d', pw), "Password must contain at least one digit."),
        (re.search(r'\W', pw), "Password must contain at least one special character.")
    ]

    for check, message in checks:
        if not check:
            return False, message
        
    return True, "Password is valid."

def register_user(username, pw):
    pw_hash = hash_pw(pw)
    try:
        cur.execute('INSERT INTO userlogin (username, password) VALUES (?, ?)', (username, pw_hash))
        con.commit()
        print("User registered successfully.")
        if not profile_exists(con, username):
            collect_profile_data(con, username)
    except sqlite3.IntegrityError:
        print("Username already exists. Please try again.")
        return False

def verify_user(username, pw):
    cur.execute('SELECT password FROM userlogin WHERE username = ?', (username,))
    stored_pw = cur.fetchone()
    if stored_pw:
        print(f"Debug: Stored password hash: {stored_pw[0]}")  # Debug print
        if bcrypt.checkpw(pw.encode('utf-8'), stored_pw[0].encode('utf-8')):
            return True
        else:
            print("Password does not match.")
            return False
    else:
        print("Username not found.")
        return False

def welcomeback(username):
    print("Welcome back! You are now logged in.")
    display_user_info(con, username)

# cleartable is for debugging purposes only
def cleartable():
    cur.execute('DELETE FROM userlogin')
    cur.execute('DELETE FROM userprofile')
    con.commit()
    print("Table cleared.")

print("Starting the program")

print("Welcome to reImagine! Please register or login to continue.")
choice = input("Enter '1' to register, '2' to login, or '3' to clear the database: ").strip()

if choice == '1':
    print("Registering a new user...")
    username = input("Enter your username: ").strip()
    pw = input("Enter your password: ").strip()
    valid_pw, message = validate_pw(pw)
    while not valid_pw:
        print(message)
        pw = input("Enter your password: ").strip()
        valid_pw, message = validate_pw(pw)
    register_user(username, pw)
        
elif choice == '2':
    print("Logging in...")
    username = input("Enter your username: ").strip()
    pw = input("Enter your password: ").strip()
    if verify_user(username, pw):
        print("Login successful!")
        welcomeback(username)
    else:
        print("Invalid username or password. Please try again.")
else:
    print("Invalid choice. Please enter '1' or '2'.")
"""    
elif choice == '3':
    print("Clearing the database...")
    cleartable()
"""


