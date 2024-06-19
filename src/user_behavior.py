# src/user_behavior.py

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Simulated user interaction data
user_ids = ['user1', 'user2', 'user3']
video_ids = ['video1', 'video2', 'video3']
interactions = [
    ('user1', 'video1'), 
    ('user1', 'video2'), 
    ('user2', 'video2'), 
    ('user3', 'video3')
]

# Encode user and video IDs
user_encoder = LabelEncoder()
video_encoder = LabelEncoder()
user_ids_encoded = user_encoder.fit_transform([x[0] for x in interactions])
video_ids_encoded = video_encoder.fit_transform([x[1] for x in interactions])

# Prepare data for RNN
X = np.array([user_ids_encoded, video_ids_encoded]).T
y = np.random.rand(len(interactions))  # Random ratings for example

# Define RNN model
model = Sequential()
model.add(Embedding(input_dim=len(user_encoder.classes_), output_dim=50, input_length=2))
model.add(LSTM(50))
model.add(Dense(1, activation='linear'))
model.compile(optimizer='adam', loss='mse')

# Train RNN model
model.fit(X, y, epochs=10, batch_size=2)

# Example prediction
example_user = user_encoder.transform(['user1'])
example_video = video_encoder.transform(['video3'])
prediction = model.predict(np.array([[example_user, example_video]]))
print(prediction)
