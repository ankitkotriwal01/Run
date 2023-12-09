import streamlit as st
import requests
from requests.auth import HTTPBasicAuth

# Function to get song recommendations based on user input using Jamendo API
def get_recommendations(genre, mood):
    # Define Jamendo API endpoint
    jamendo_url = "https://api.jamendo.com/v3.0/tracks/"

    # Authentication credentials
    client_id = "c7638456"
    client_secret = "2813a50987edc8819c4c4fed55e30e83"

    # Set up authentication
    auth = HTTPBasicAuth(client_id, client_secret)

    # Make a request to the Jamendo API based on user input
    jamendo_params = {
        "format": "json",
        "limit": 10,  # Adjust the limit as needed
        "tags": f"{genre} {mood}"
    }

    # Make a request to Jamendo API with authentication
    jamendo_response = requests.get(jamendo_url, params=jamendo_params, auth=auth)

    # Print the JSON response for debugging
    st.write("Jamendo Response:", jamendo_response.json())

    # Extract track recommendations from the response
    try:
        jamendo_recommendations = [track["name"] for track in jamendo_response.json()["results"]]
    except KeyError:
        st.error("Error: Unable to extract recommendations from the Jamendo API response.")
        return {"Jamendo": []}

    return {"Jamendo": jamendo_recommendations}

# Streamlit UI
st.title("Music Recommendation App")
genre = st.selectbox("Select Genre:", ["pop", "rock", "hip hop", "electronic", "jazz", "country", "blues", "reggae", "classical", "metal",
                                       "folk", "indie", "rap", "latin", "punk", "r&b", "soul", "dance", "ambient", "disco", "funk",
                                       "gospel", "reggaeton", "techno", "trap", "house", "ska", "grunge", "dubstep", "chill", "EDM"])
mood = st.slider("Select Mood:", 0.0, 1.0, 0.5, 0.1)

if st.button("Get Recommendations"):
    recommendations = get_recommendations(genre, mood)
    st.subheader("Recommended Songs:")

    for service, songs in recommendations.items():
        st.write(f"**{service}**:")
        for i, song in enumerate(songs, 1):
            st.write(f"{i}. {song}")

        # No play button for simplicity since we're using Jamendo

        st.write("\n")
