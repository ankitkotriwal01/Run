import streamlit as st

# Function to initialize the counter if it doesn't exist
def initialize_counter():
    if 'application_counter' not in st.session_state:
        st.session_state.application_counter = 0

# Main function to display the application counter and buttons
def job_application_counter():
    st.title('Job Application Counter')

    # Initialize the counter
    initialize_counter()

    # Display the current application count
    st.subheader('Current Applications: {}'.format(st.session_state.application_counter))

    # Buttons for incrementing and resetting the counter
    if st.button('Apply for a Job'):
        st.session_state.application_counter += 1

    if st.button('Reset Counter'):
        st.session_state.application_counter = 0

# Run the app
if __name__ == '__main__':
    job_application_counter()
