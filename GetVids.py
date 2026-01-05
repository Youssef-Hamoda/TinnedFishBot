import json
from googleapiclient.discovery import build

# Load API key from config
with open('config.json', 'r') as f:
    config = json.load(f)

DEVELOPER_KEY = config['yt_api']
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def get_service():
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                   developerKey=DEVELOPER_KEY)
    return youtube

def get_vid_ids():
    youtube = get_service()
    
    try:
        search_response = youtube.search().list(
            part='snippet',
            channelId='UCnM8PMUe_Kmp4-Ohq4V7Vdw',
            type='video',
            maxResults=1,
            videoDuration='short',
            order='rating',
        ).execute()
        
        videos = []
        
        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                videos.append([search_result['id']['videoId'], search_result['snippet']['title']])
        
    except Exception as e:
        print(f"Error: {e}")
        return []
    
    return videos

if __name__ == '__main__':
    video_ids = get_vid_ids()
    print(json.dumps(video_ids))
