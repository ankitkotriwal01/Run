import streamlit as st
import sqlite3

# Create SQLite database and table for users
conn_users = sqlite3.connect('user_database.db')
c_users = conn_users.cursor()
c_users.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        role TEXT
    )
''')
conn_users.commit()

# Function to add a user
def add_user(name, role):
    c_users.execute('INSERT INTO users (name, role) VALUES (?, ?)', (name, role))
    conn_users.commit()

# Function to delete a user
def delete_user(user_id):
    c_users.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn_users.commit()

# Function to modify a user
def modify_user(user_id, name, role):
    c_users.execute('UPDATE users SET name = ?, role = ? WHERE id = ?', (name, role, user_id))
    conn_users.commit()

# Function to display all users
def display_users():
    users = c_users.execute('SELECT * FROM users').fetchall()
    return users

# Streamlit UI
st.title('User Database Management')

# Add User Section
st.header('Add User')
user_name = st.text_input('Name:')
user_role = st.selectbox('Role:', ['Recruiter', 'Jobseeker'])
if st.button('Add User'):
    add_user(user_name, user_role)

# Delete User Section
st.header('Delete User')
delete_user_id = st.number_input('User ID to delete:')
if st.button('Delete User'):
    delete_user(delete_user_id)

# Modify User Section
st.header('Modify User')
modify_user_id = st.number_input('User ID to modify:')
modify_user_name = st.text_input('New Name:')
modify_user_role = st.selectbox('New Role:', ['Recruiter', 'Jobseeker'])
if st.button('Modify User'):
    modify_user(modify_user_id, modify_user_name, modify_user_role)

# Display Users Section
st.header('Display Users')
users = display_users()
st.write(users)
