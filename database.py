import streamlit as st
import sqlite3
import pandas as pd

def upload_recruiters_from_excel(file_path):
    try:
        # Read the Excel file into a Pandas DataFrame
        recruiters_df = pd.read_excel(file_path)

        # Fill missing values with an empty string
        recruiters_df = recruiters_df.fillna('')

        # Connect to the database
        connection = sqlite3.connect('job_portals.db')
        cursor = connection.cursor()

        # Insert each recruiter from the DataFrame into the database
        for index, recruiter in recruiters_df.iterrows():
            cursor.execute('''
                INSERT INTO recruiters ("first_name", "second_name", "company", "email", "sector", "phone", "job_title",
                                       "linkedin_profile", "certifications", "target_regions", "target_cities",
                                       "designation", "company_description", "social_media_links")
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (recruiter['first_name'], recruiter['second_name'], recruiter['company'],
                  recruiter['email'], recruiter['sector'], recruiter['phone'], recruiter['job_title'],
                  recruiter['linkedin_profile'], recruiter['certifications'], recruiter['target_regions'],
                  recruiter['target_cities'], recruiter['designation'], recruiter['company_description'],
                  recruiter['social_media_links']))

        # Commit changes and close the connection
        connection.commit()
        connection.close()

        st.success("Recruiters uploaded successfully!")

    except Exception as e:
        st.error(f"Error uploading recruiters: {e}")


def add_job_with_details(title, description, recruiter_id, qualifications, location, company_info,
                         application_instructions, salary_benefits, deadline, equal_opportunity_statement,
                         contact_information, company_culture_values, application_form_link):
    connection = sqlite3.connect('job_available.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO jobs ("title", "description", "recruiter_id", "qualifications", "location", "company_info",
                         "application_instructions", "salary_benefits", "deadline", "equal_opportunity_statement",
                         "contact_information", "company_culture_values", "application_form_link")
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (title, description, recruiter_id, qualifications, location, company_info,
          application_instructions, salary_benefits, deadline, equal_opportunity_statement,
          contact_information, company_culture_values, application_form_link))

    connection.commit()
    connection.close()
# Function to initialize the database
def initialize_database():
    connection = sqlite3.connect('job_portals.db')
    cursor = connection.cursor()

    # Recruiters table
    # Recruiters table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recruiters (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            second_name TEXT NOT NULL,
            company TEXT NOT NULL,
            email TEXT NOT NULL,
            sector TEXT NOT NULL,
            phone TEXT,
            job_title TEXT,
            linkedin_profile TEXT,
            certifications TEXT,
            target_regions TEXT,
            target_cities TEXT,
            designation TEXT,
            company_description TEXT,
            social_media_links TEXT
        )
    ''')

    connection.commit()
    connection.close()


def initialize_database():
    connection = sqlite3.connect('job_seekers.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS job_seekers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            skills TEXT NOT NULL,
            email TEXT NOT NULL,
            certifications TEXT NOT NULL,
            professional_experience TEXT NOT NULL,
            finance_specialization TEXT NOT NULL,
            skills_languages TEXT NOT NULL,
            memberships TEXT NOT NULL,
            location_preferences TEXT NOT NULL,
            job_preferences TEXT NOT NULL,
            portfolio_link TEXT NOT NULL,
            salary_expectations TEXT NOT NULL,
            personal_statement TEXT NOT NULL,
            availability TEXT NOT NULL
        )
    ''')



# Jobs table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            recruiter_id INTEGER,
            FOREIGN KEY (recruiter_id) REFERENCES recruiters(id)
        )
    ''')

    connection.commit()
    connection.close()

# Function to add a recruiter to the database
def add_recruiter(first_name, second_name, company, email, sector, phone, job_title,
                  linkedin_profile, certifications, target_regions, target_cities, designation,
                  company_description, social_media_links):
    connection = sqlite3.connect('job_portals.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO recruiters (first_name, second_name, company, email, sector, phone, job_title, '
                   'linkedin_profile, certifications, target_regions, target_cities, designation, '
                   'company_description, social_media_links) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   (first_name, second_name, company, email, sector, phone, job_title,
                    linkedin_profile, certifications, target_regions, target_cities, designation,
                    company_description, social_media_links))

    connection.commit()
    connection.close()

# Function to add a job seeker to the database
# Function to add a job seeker to the database
# Function to add a job seeker to the database
def add_job_seeker(name, skills, email, certifications, professional_experience,
                   finance_specialization, skills_languages, memberships, location_preferences,
                   job_preferences, portfolio_link, salary_expectations,
                   personal_statement, availability):
    connection = sqlite3.connect('job_seekers.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO job_seekers ("name", "skills", "email", "certifications",
                                  "professional_experience", "finance_specialization",
                                  "skills_languages", "memberships", "location_preferences",
                                  "job_preferences", "portfolio_link", 
                                  "salary_expectations", "personal_statement", "availability")
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, skills, email, certifications, professional_experience,
          finance_specialization, skills_languages, memberships, location_preferences,
          job_preferences, portfolio_link, salary_expectations,
          personal_statement, availability))

    connection.commit()
    connection.close()


# Function to add a job seeker to the database
def add_job_seeker_to_database(name, skills, email, certifications, professional_experience,
                               finance_specialization, skills_languages, memberships, location_preferences,
                               job_preferences, portfolio_link, salary_expectations,
                               personal_statement, availability):
    connection = sqlite3.connect('job_seekers.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO job_seekers ("name", "skills", "email",  "certifications",
                                  "professional_experience", "finance_specialization",
                                  "skills_languages", "memberships", "location_preferences",
                                  "job_preferences", "portfolio_link", 
                                  "salary_expectations", "personal_statement", "availability")
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, skills, email, certifications, professional_experience,
          finance_specialization, skills_languages, memberships, location_preferences,
          job_preferences, portfolio_link, salary_expectations,
          personal_statement, availability))

    connection.commit()
    connection.close()


# Function to add a job to the database
def add_job(title, description, recruiter_id):
    connection = sqlite3.connect('job_available.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO jobs (title, description, recruiter_id) VALUES (?, ?, ?)',
                   (title, description, recruiter_id))

    connection.commit()
    connection.close()

# Function to display available jobs
def display_jobs():
    connection = sqlite3.connect('job_portals.db')
    cursor = connection.cursor()

    cursor.execute('''
        SELECT jobs.id, title, description, recruiters.name as recruiter_name
        FROM jobs
        JOIN recruiters ON jobs.recruiter_id = recruiters.id
    ''')

    jobs = cursor.fetchall()
    connection.close()

    st.subheader("Available Jobs:")
    for job in jobs:
        st.write(f"Job ID: {job[0]}, Title: {job[1]}, Description: {job[2]}, Recruiter: {job[3]}")

import streamlit as st
import sqlite3
import pandas as pd

import streamlit as st
import sqlite3
import pandas as pd


# Test the function
import streamlit as st
import sqlite3
import pandas as pd

def display_recruiters():
    connection = sqlite3.connect('job_portals.db')
    cursor = connection.cursor()

    # Fetch the list of column names
    cursor.execute("PRAGMA table_info('recruiters')")
    columns_info = cursor.fetchall()
    columns = [column[1] for column in columns_info]

    # Display column selection checkboxes
    selected_columns = st.multiselect("Select columns to display", columns, default=columns)

    # Create the SELECT query based on selected columns
    select_query = f"SELECT {', '.join(selected_columns)} FROM recruiters"

    # Execute the query
    cursor.execute(select_query)
    recruiters_data = cursor.fetchall()

    # Create a DataFrame from the fetched data
    recruiters_df = pd.DataFrame(recruiters_data, columns=selected_columns)

    connection.close()

    st.subheader("List of Recruiters:")

    # Dynamic filters based on user input
    for column in selected_columns:
        if st.checkbox(f"Filter by {column}"):
            # Apply filter based on column type
            if recruiters_df[column].dtype == 'O':  # Object type (categorical)
                filter_value = st.selectbox(f"Select value for {column}", recruiters_df[column].unique())
                recruiters_df = recruiters_df[recruiters_df[column] == filter_value]
            elif recruiters_df[column].dtype in ['int64', 'float64']:  # Numerical type
                min_value, max_value = st.slider(f"Select range for {column}", float(recruiters_df[column].min()), float(recruiters_df[column].max()), (float(recruiters_df[column].min()), float(recruiters_df[column].max())))
                recruiters_df = recruiters_df[(recruiters_df[column] >= min_value) & (recruiters_df[column] <= max_value)]

    # Display the filtered DataFrame
    st.dataframe(recruiters_df)

    selected_rows = st.multiselect("Select rows for deletion", recruiters_df.index)

    if st.button("Delete Selected Recruiters"):
        # Delete selected recruiters from the DataFrame
        recruiters_df = recruiters_df.drop(index=selected_rows)

        # Update the database with the modified DataFrame
        update_recruiters_in_database(recruiters_df)

        st.success("Selected recruiters deleted successfully!")

# Test the function


# Test the function

def display_job_seekers():
    connection = sqlite3.connect('job_seekers.db')
    cursor = connection.cursor()

    # Fetch the list of column names
    cursor.execute("PRAGMA table_info('job_seekers')")
    columns_info = cursor.fetchall()
    columns = [column[1] for column in columns_info]

    # Display column selection checkboxes
    selected_columns = st.multiselect("Select columns to display", columns, default=columns)

    # Create the SELECT query based on selected columns
    select_query = f"SELECT {', '.join(selected_columns)} FROM job_seekers"

    # Execute the query
    cursor.execute(select_query)
    job_seekers_data = cursor.fetchall()

    # Create a DataFrame from the fetched data
    job_seekers_df = pd.DataFrame(job_seekers_data, columns=selected_columns)

    connection.close()

    st.subheader("List of Job Seekers:")

    # Dynamic filters based on user input
    for column in selected_columns:
        if st.checkbox(f"Filter by {column}"):
            # Apply filter based on column type
            if job_seekers_df[column].dtype == 'O':  # Object type (categorical)
                filter_value = st.selectbox(f"Select value for {column}", job_seekers_df[column].unique())
                job_seekers_df = job_seekers_df[job_seekers_df[column] == filter_value]
            elif job_seekers_df[column].dtype in ['int64', 'float64']:  # Numerical type
                min_value, max_value = st.slider(f"Select range for {column}", float(job_seekers_df[column].min()), float(job_seekers_df[column].max()), (float(job_seekers_df[column].min()), float(job_seekers_df[column].max())))
                job_seekers_df = job_seekers_df[(job_seekers_df[column] >= min_value) & (job_seekers_df[column] <= max_value)]

    # Display the filtered DataFrame
    st.dataframe(job_seekers_df)

    selected_rows = st.multiselect("Select rows for deletion", job_seekers_df.index)

    if st.button("Delete Selected Job Seekers"):
        # Delete selected job seekers from the DataFrame
        job_seekers_df = job_seekers_df.drop(index=selected_rows)

        # Update the database with the modified DataFrame
        update_job_seekers_in_database(job_seekers_df)

        st.success("Selected job seekers deleted successfully!")


def update_recruiters_in_database(recruiters_df):
    connection = sqlite3.connect('job_portals.db')
    cursor = connection.cursor()

    # Drop and recreate the recruiters table
    cursor.execute('DROP TABLE IF EXISTS recruiters')
    initialize_database()

    # Insert the modified DataFrame into the database
    recruiters_df.to_sql('recruiters', connection, index=False, if_exists='replace')

    connection.commit()
    connection.close()

def update_job_seekers_in_database(job_seekers_df):
    connection = sqlite3.connect('job_seekers.db')
    cursor = connection.cursor()

    # Drop and recreate the job_seekers table
    cursor.execute('DROP TABLE IF EXISTS job_seekers')
    initialize_database()

    # Insert the modified DataFrame into the database
    job_seekers_df.to_sql('job_seekers', connection, index=False, if_exists='replace')

    connection.commit()
    connection.close()

# Main Streamlit app
def main():
    initialize_database()

    st.title("Mob - Finance Network ")

    menu_options = ["Add Recruiter", "Add Job Seeker", "Add Job", "Display Recruiters", "Display Job Seekers", "Display Jobs","Upload Recruiters"]
    choice = st.sidebar.selectbox("Choose an option", menu_options)

    if choice == "Add Recruiter":
        st.subheader("Add Recruiter")
        first_name = st.text_input("Enter recruiter's first name:")
        last_name = st.text_input("Enter recruiter's last name:")
        company = st.text_input("Enter company name:")
        email = st.text_input("Enter email:")
        sector = st.text_input("Enter sector:")
        phone = st.text_input("Enter phone (optional):")
        job_title = st.text_input("Enter job title (optional):")
        linkedin_profile = st.text_input("Enter LinkedIn profile (optional):")
        certifications = st.text_input("Enter certifications (optional):")
        target_regions = st.text_input("Enter target regions :")
        target_cities = st.text_input("Enter target cities :")
        designation = st.text_input("Enter designation :")
        company_description = st.text_input("Enter company description (optional):")
        social_media_links = st.text_input("Enter social media links (optional):")

        if st.button("Add Recruiter"):
                add_recruiter(first_name, last_name, company, email,sector,phone,job_title,linkedin_profile,certifications,target_regions,target_cities,designation,company_description,social_media_links)
                st.success("Recruiter added successfully!")

    elif choice == "Add Job Seeker":
        st.subheader("Add Job Seeker")

        # Input fields
        name = st.text_input("Name:")
        skills = st.text_input("Skills (comma-separated):")
        email = st.text_input("Email:")
        certifications = st.text_input("Certifications:")
        professional_experience = st.text_input("Professional Experience:")
        finance_specialization = st.text_input("Finance Specialization:")
        skills_languages = st.text_input("Skills & Languages:")
        memberships = st.text_input("Memberships:")
        location_preferences = st.text_input("Location Preferences:")
        job_preferences = st.text_input("Job Preferences:")
        portfolio_link = st.text_input("Portfolio Link:")
        salary_expectations = st.text_input("Salary Expectations:")
        personal_statement = st.text_input("Personal Statement:")
        availability = st.text_input("Availability:")

        if st.button("Add Job Seeker"):
            # Add job seeker to the database
            add_job_seeker(name, skills, email, certifications, professional_experience,
                           finance_specialization, skills_languages, memberships, location_preferences,
                           job_preferences, portfolio_link, salary_expectations,
                           personal_statement, availability)
            st.success("Job Seeker added successfully!")



    elif choice == "Add Job":
        st.subheader("Add Job")
        title = st.text_input("Enter job title:")
        description = st.text_input("Enter job description:")
        recruiter_id = st.number_input("Enter recruiter ID:")
        if st.button("Add Job"):
            add_job(title, description, recruiter_id)
            st.success("Job added successfully!")

    elif choice == "Display Recruiters":
        display_recruiters()

    elif choice == "Display Job Seekers":
        display_job_seekers()

    elif choice == "Display Jobs":
        display_jobs()

    elif choice == "Upload Recruiters":
        st.subheader("Upload Recruiters from Excel")
        uploaded_file = st.file_uploader("Choose an Excel file", type=["xls", "xlsx"])

        if uploaded_file is not None:
            upload_recruiters_from_excel(uploaded_file)


if __name__ == "__main__":
    main()
