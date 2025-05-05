import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

def predict_next_day_price(df):
    if len(df) < 60:
        return df["Close"].iloc[-1]  # fallback if not enough data

    # Sort by date and reset index
    df = df.sort_values("Date").reset_index(drop=True)
    close_data = df["Close"].values.reshape(-1, 1)

    # Normalize data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(close_data)

    # Create input/output sequences
    X = []
    y = []
    for i in range(60, len(scaled_data)):
        X.append(scaled_data[i-60:i])
        y.append(scaled_data[i])

    X = np.array(X)
    y = np.array(y)

    # Define LSTM model
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)))
    model.add(LSTM(50))
    model.add(Dense(1))
    model.compile(optimizer="adam", loss="mean_squared_error")

    # Train model
    model.fit(X, y, epochs=5, batch_size=32, verbose=0)

    # Prepare last 60 days for prediction
    last_60_days = scaled_data[-60:]
    last_60_days = np.expand_dims(last_60_days, axis=0)

    # Predict and inverse transform
    prediction = model.predict(last_60_days)
    predicted_price = scaler.inverse_transform(prediction)

    return float(predicted_price[0][0])
