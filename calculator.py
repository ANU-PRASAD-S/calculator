import streamlit as st
from googleapiclient.discovery import build

# Function to get YouTube channel data
def get_youtube_channel_data(api_key, channel_id):
  youtube = build('youtube', 'v3', developerKey=api_key)
  request = youtube.channels().list(
      part="snippet,contentDetails,statistics",
      id=channel_id
  )
  response = request.execute()
  return response

# Title of the app
st.title("YouTube Channel Data Retriever")

# Section for entering API token
st.header("Enter API Token")
api_token = st.text_input("API Token")
#api_key = "api_token"

# Section for entering YouTube channel ID
st.header("Enter YouTube Channel ID")
channel_id = st.text_input("YouTube Channel ID")

# Button to submit the form and fetch data
if st.button("Submit"):
  if api_token and channel_id:
    try:
      channel_data = get_youtube_channel_data(api_key, channel_id)
      st.success("Successfully retrieved channel data!")

      # Check for valid data
      if 'items' in channel_data and len(channel_data['items']) > 0:
        channel_info = channel_data['items'][0]

        # Display basic channel info
        st.subheader("Channel Information")
        st.write(f"**Title:** {channel_info['snippet']['title']}")
        st.write(f"**Description:** {channel_info['snippet']['description']}")
        st.write(f"**Published At:** {channel_info['snippet']['publishedAt']}")
        st.write(f"**Subscribers:** {channel_info['statistics']['subscriberCount']}")
        st.write(f"**Total Views:** {channel_info['statistics']['viewCount']}")
        st.write(f"**Total Videos:** {channel_info['statistics']['videoCount']}")
      else:
        st.warning("No channel data found for the given ID.")
    except Exception as e:
      st.error(f"An error occurred: {e}")
  else:
    st.error("Please enter both the API Token and YouTube Channel ID.")

