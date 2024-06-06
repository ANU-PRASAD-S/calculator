import streamlit as st

# Title of the app
st.title("YouTube API Token and Channel ID Entry")

# Section for entering API token
st.header("Enter API Token")
api_token = st.text_input("API Token", type="password")

# Section for entering YouTube channel ID
st.header("Enter YouTube Channel ID")
channel_id = st.text_input("YouTube Channel ID")

# Display the entered values
if st.button("Submit"):
    if api_token and channel_id:
        st.success(f"API Token: {api_token}")
        st.success(f"YouTube Channel ID: {channel_id}")
    else:
        st.error("Please enter both the API Token and YouTube Channel ID.")

