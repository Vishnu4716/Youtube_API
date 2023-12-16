#21BAI1564-G SAI VISHNUVARDHAN REDDY
#21BEC1041-P HARI KRISHNA REDDY
from googleapiclient.discovery import build

api_key = 'AIzaSyA20G1c9UVQJmmlm_QASrpDI_lmqpCuE-8'
youtube = build('youtube', 'v3', developerKey=api_key)
#api_service_name = "youtube"
#api_version = "v3"
channel_id = 'UCQYMhOMi_Cdj1CEAU-fv80A'#NESO-ACADEMY CHANNEL ID

# Get the video list from the channel
search_response = youtube.search().list(
    part='id',
    channelId=channel_id,
    type='video',
).execute()

# Extract video IDs from the search results
video_ids = [item['id']['videoId'] for item in search_response['items']]

# Get comments for each video
for vid in video_ids:
    comments_response = youtube.commentThreads().list(
        part='snippet',
        videoId=vid,
    ).execute()

    # Extract and print comments
    for item in comments_response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        print(comment)
