# src/main.py

from data_collection import initialize_youtube, get_video_data
from feature_extraction import extract_frames, extract_features
from user_behavior import user_encoder, video_encoder, model as rnn_model
from recommendation import matrix_factorization, neural_collaborative_filtering
from model_optimization import grid_result

def main():
    # Initialize YouTube API
    api_key = 'YOUR_ACTUAL_YOUTUBE_API_KEY'
    youtube = initialize_youtube(api_key)

    # Collect video data
    video_data = get_video_data(youtube, 'short videos', max
