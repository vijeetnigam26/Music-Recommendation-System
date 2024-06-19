# src/recommendation.py

from scipy.sparse.linalg import svds
import numpy as np
from tensorflow.keras.layers import Input, Embedding, Flatten, Dot, Concatenate, Dense
from tensorflow.keras.models import Model

# Matrix Factorization

def matrix_factorization(interaction_matrix, k=2):
    U, sigma, Vt = svds(interaction_matrix, k=k)
    sigma = np.diag(sigma)
    predicted_matrix = np.dot(np.dot(U, sigma), Vt)
    return predicted_matrix

# Example user-item interaction matrix
interaction_matrix = np.array([
    [5, 3, 0],
    [4, 0, 0],
    [1, 1, 0]
])

predicted_matrix = matrix_factorization(interaction_matrix)
print(predicted_matrix)

# Neural Collaborative Filtering

def neural_collaborative_filtering(num_users, num_videos):
    user_input = Input(shape=(1,))
    video_input = Input(shape=(1,))

    user_embedding = Embedding(num_users, 50)(user_input)
    video_embedding = Embedding(num_videos, 50)(video_input)

    user_vec = Flatten()(user_embedding)
    video_vec = Flatten()(video_embedding)

    concat = Concatenate()([user_vec, video_vec])
    dense = Dense(128, activation='relu')(concat)
    output = Dense(1, activation='linear')(dense)

    model = Model([user_input, video_input], output)
    model.compile(optimizer='adam', loss='mse')

    return model

# Example usage
if __name__ == "__main__":
    num_users = len(user_encoder.classes_)
    num_videos = len(video_encoder.classes_)
    model = neural_collaborative_filtering(num_users, num_videos)
    model.fit([user_ids_encoded, video_ids_encoded], y, epochs=10, batch_size=2)
    prediction = model.predict([example_user, example_video])
    print(prediction)
