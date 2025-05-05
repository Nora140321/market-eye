import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

def predict_next_day_price(df):
    data = df["Close"].values.reshape(-1, 1)
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data)

    x, y = [], []
    for i in range(60, len(scaled_data)):
        x.append(scaled_data[i-60:i, 0])
        y.append(scaled_data[i, 0])

    x, y = np.array(x), np.array(y)
    x = x.reshape((x.shape[0], x.shape[1], 1))

    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(x.shape[1], 1)))
    model.add(LSTM(50))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x, y, epochs=10, batch_size=16, verbose=0)

    last_60 = scaled_data[-60:].reshape(1, 60, 1)
    predicted_scaled = model.predict(last_60, verbose=0)
    predicted_price = scaler.inverse_transform(predicted_scaled)[0][0]
    return predicted_price
