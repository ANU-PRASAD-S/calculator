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

# Function to get details of a specific video
def get_video_details(api_key, video_id):
  youtube = build('youtube', 'v3', developerKey=api_key)
  video_request = youtube.videos().list(
      part="snippet,statistics",
      id=video_id
  )
  video_response = video_request.execute()
  return video_response

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

      # Create a container for the main content (center section)
      main_content = st.container()

      # Create a container for the side section
      side_section = st.sidebar

      # Display channel information in the main content (unchanged)
      with main_content:
          if 'items' in channel_response and len(channel_response['items']) > 0:
              channel_info = channel_response['items'][0]
              st.subheader("Channel Information")
              # ... (rest of your channel info display code)

      # Display video information in the side section (if available)
      if video_response:
          side_section.subheader("Recent Videos")
          for item in video_response['items']:
              video_id = item['snippet']['resourceId']['videoId']
              video_title = item['snippet']['title']

              # Get detailed video statistics
              video_details_response = get_video_details(api_key, video_id)
              if 'items' in video_details_response and len(video_details_response['items']) > 0:
                  video_details = video_details_response['items'][0]
                  view_count = video_details['statistics'].get('viewCount', 0)
                  like_count = video_details['statistics'].get('likeCount', 0)
                  comment_count = video_details['statistics'].get('commentCount', 0)
                  
                  # Create a dictionary to store video data
                  video_data = {
                      'video_id': video_id,
                      'video_title': video_title,
                      # ... (add other video info from previous code)
                      'view_count': view_count,
                      'like_count': like_count,
                      'comment_count': comment_count
                  }
                  
                  # Display video data (including play count, likes, comments)
                  side_section.write(f"- {video_title} (Views: {view_count}, Likes: {like_count}, Comments: {comment_count})")
              else:
                  side_section.write(f"- {video_title} (Details

                        # Display remaining channel information in the main content (text format)
      with main_content:
          if 'items' in channel_response and len(channel_response['items']) > 0:
              channel_info = channel_response['items'][0]
              st.subheader("Channel Information")
              st.write(f"Description: {channel_info['snippet']['description']}")
              st.write(f"Subscribers: {channel_info['statistics']['subscriberCount']}")
              # Add similar lines for other desired channel statistics


