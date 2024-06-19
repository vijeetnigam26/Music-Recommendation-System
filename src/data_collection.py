# src/data_collection.py

from googleapiclient.discovery import build
import pandas as pd

def initialize_youtube(api_key):
    return build('youtube', 'v3', developerKey=api_key)

def search_videos(youtube, query, max_results=50):
    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=max_results
    )
    response = request.execute()
    return response['items']

def get_video_details(youtube, video_ids):
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=','.join(video_ids)
    )
    response = request.execute()
    return response['items']

def get_video_data(youtube, query, max_results=50):
    search_results = search_videos(youtube, query, max_results)
    video_ids = [item['id']['videoId'] for item in search_results]
    video_details = get_video_details(youtube, video_ids)
    
    videos_data = []
    for video in video_details:
        video_data = {
            'video_id': video['id'],
            'title': video['snippet']['title'],
            'description': video['snippet']['description'],
            'channel_title': video['snippet']['channelTitle'],
            'published_at': video['snippet']['publishedAt'],
            'view_count': video['statistics'].get('viewCount', 0),
            'like_count': video['statistics'].get('likeCount', 0),
            'dislike_count': video['statistics'].get('dislikeCount', 0),
            'comment_count': video['statistics'].get('commentCount', 0),
            'duration': video['contentDetails']['duration'],
            'tags': video['snippet'].get('tags', [])
        }
        videos_data.append(video_data)
    
    return pd.DataFrame(videos_data)

if __name__ == "__main__":
    api_key = 'YOUR_ACTUAL_YOUTUBE_API_KEY'
    youtube = initialize_youtube(api_key)
    video_data = get_video_data(youtube, 'short videos', max_results=10)
    print(video_data.head())
