import pandas as pd
import os

INPUT_PATH = "C:/Users/Noura/OneDrive/Desktop/python proj/61/World-Stock-Prices-Dataset.csv"
OUTPUT_DIR = "C:/Users/Noura/OneDrive/Desktop/python proj/61/data"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "cleaned_stock_data.csv")

def load_and_clean_stock_data():
    df = pd.read_csv(INPUT_PATH)
    print("Available columns:", df.columns.tolist())

    # Use 'Ticker' instead of 'Symbol'
    required_columns = ['Ticker', 'Date']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        print(f"Missing columns: {missing_columns}")
        return

    df.dropna(inplace=True)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.dropna(subset=['Date'], inplace=True)
    df.sort_values(by=['Ticker', 'Date'], inplace=True)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"\n✅ Cleaned data saved to: {OUTPUT_PATH}")

if __name__ == "__main__":
    load_and_clean_stock_data()
