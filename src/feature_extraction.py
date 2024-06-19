# src/feature_extraction.py

import cv2
import numpy as np
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input

# Initialize the ResNet model
model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

def extract_frames(video_path, num_frames=10):
    cap = cv2.VideoCapture(video_path)
    frames = []
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_interval = max(1, total_frames // num_frames)
    
    for i in range(num_frames):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i * frame_interval)
        ret, frame = cap.read()
        if ret:
            frames.append(frame)
        else:
            print(f"Frame {i * frame_interval} could not be read.")
            break
    
    cap.release()
    return frames

def extract_features(frames):
    if not frames:
        print("No frames extracted.")
        return np.array([])
    
    frame_features = []
    for frame in frames:
        img = cv2.resize(frame, (224, 224))
        img = preprocess_input(img)
        img = np.expand_dims(img, axis=0)
        features = model.predict(img)
        frame_features.append(features.flatten())
    
    if not frame_features:
        print("No features extracted from frames.")
        return np.array([])
    
    return np.mean(frame_features, axis=0)

# Example usage
if __name__ == "__main__":
    video_path = 'path_to_video_file.mp4'
    frames = extract_frames(video_path)
    print(f"Number of frames extracted: {len(frames)}")
    for idx, frame in enumerate(frames):
        print(f"Frame {idx} shape: {frame.shape}")
    
    video_features = extract_features(frames)
    if video_features.size:
        print(f"Extracted video features shape: {video_features.shape}")
    else:
        print("No video features extracted.")
