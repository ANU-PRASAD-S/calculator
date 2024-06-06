import streamlit as st
from googleapiclient.discovery import build

# Function to get YouTube channel data
def get_youtube_channel_data(api_key, channel_id):
  youtube = build('youtube', 'v3', developerKey=api_key)
  
  # Request for channel data
  channel_request = youtube.channels().list(
      part="snippet,contentDetails,statistics",
      id=channel_id
  )
  channel_response = channel_request.execute()
  
  # Request for video data (if channel exists)
  if 'items' in channel_response and len(channel_response['items']) > 0:
      upload_playlist_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
      video_request = youtube.playlistItems().list(
          part="snippet",
          playlistId=upload_playlist_id,
          maxResults=50  # Adjust this to retrieve a desired number of videos
      )
      video_response = video_request.execute()
      return channel_response, video_response
  else:
      return channel_response, None

# Title of the app
st.title("YouTube Channel Data Retriever")

# Section for entering API token
st.header("Enter API Token")
api_key = st.text_input("API Token", type="password")

# Section for entering YouTube channel ID
st.header("Enter YouTube Channel ID")
channel_id = st.text_input("YouTube Channel ID")

# Button to submit the form and fetch data
if st.button("Submit"):
  if api_key and channel_id:
    try:
      channel_response, video_response = get_youtube_channel_data(api_key, channel_id)
      st.success("Successfully retrieved channel data!")

      # Display channel information (unchanged)
      if 'items' in channel_response and len(channel_response['items']) > 0:
          channel_info = channel_response['items'][0]
          st.subheader("Channel Information")
          # ... (rest of your channel info display code)

      # Display video information (if available)
      if video_response:
          st.subheader("Recent Videos")
          for item in video_response['items']:
              video_id = item['snippet']['resourceId']['videoId']
              video_title = item['snippet']['title']
              # Make another API request to get specific video details (optional)
              # ... (code to retrieve play count, likes, comments using video_id)
              st.write(f"- {video_title}")  # Display only video title for now
    except Exception as e:
      st.error(f"An error occurred: {e}")
  else:
    st.error("Please enter both the API Token and YouTube Channel ID.")
