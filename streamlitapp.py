# streamlit_app.py
import streamlit as st
import requests

# Define the base URL for your Flask API
BASE_URL = 'http://127.0.0.1:5000'

# Function to make API requests
def make_request(endpoint, method='GET', data=None):
    url = f"{BASE_URL}/{endpoint}"
    if method == 'GET':
        response = requests.get(url)
    elif method == 'POST':
        response = requests.post(url, json=data)
    return response.json()

# Streamlit UI for Recruiters
def recruiters_page():
    st.title('Recruiters')

    # Fetch and display recruiters
    recruiters = make_request('recruiters')
    for recruiter in recruiters:
        st.write(f"ID: {recruiter['id']}, Name: {recruiter['name']}, Email: {recruiter['email']}, Phone: {recruiter['phone']}, Company: {recruiter['company']}, Bio: {recruiter['bio']}")

# Streamlit UI for Job Seekers
def job_seekers_page():
    st.title('Job Seekers')

    # Fetch and display job seekers
    job_seekers = make_request('job_seekers')
    for job_seeker in job_seekers:
        st.write(f"ID: {job_seeker['id']}, Name: {job_seeker['name']}, Email: {job_seeker['email']}, Phone: {job_seeker['phone']}, Skills: {job_seeker['skills']}, Bio: {job_seeker['bio']}")

# Streamlit UI for Job Postings
def job_postings_page():
    st.title('Job Postings')

    # Fetch and display job postings
    job_postings = make_request('job_postings')
    for job_posting in job_postings:
        st.write(f"ID: {job_posting['id']}, Title: {job_posting['title']}, Description: {job_posting['description']}, Location: {job_posting['location']}, Salary: {job_posting['salary']}, Recruiter: {job_posting['recruiter']}")

# Main Streamlit App
def main():
    st.sidebar.title('Navigation')
    page = st.sidebar.radio("Go to", ('Recruiters', 'Job Seekers', 'Job Postings'))

    if page == 'Recruiters':
        recruiters_page()
    elif page == 'Job Seekers':
        job_seekers_page()
    elif page == 'Job Postings':
        job_postings_page()

if __name__ == '__main__':
    main()
