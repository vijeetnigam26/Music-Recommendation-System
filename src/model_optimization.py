# src/model_optimization.py

from sklearn.model_selection import GridSearchCV
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor

def create_model(optimizer='adam', units=50):
    model = Sequential()
    model.add(Embedding(input_dim=len(user_encoder.classes_), output_dim=units, input_length=2))
    model.add(LSTM(units))
    model.add(Dense(1, activation='linear'))
    model.compile(optimizer=optimizer, loss='mse')
    return model

model = KerasRegressor(build_fn=create_model, epochs=10, batch_size=2, verbose=0)

param_grid = {
    'units': [50, 100],
    'optimizer': ['adam', 'rmsprop']
}

grid = GridSearchCV(estimator=model, param_grid=param_grid, cv=3)
grid_result = grid.fit(X, y)

print(f"Best: {grid_result.best_score_} using {grid_result.best_params_}")
