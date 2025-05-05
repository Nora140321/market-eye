import os
import zipfile
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# Authenticate
api = KaggleApi()
api.authenticate()

# Dataset info
dataset = "nelgiriyewithana/world-stock-prices-daily-updating"
download_path = "C:/Users/Noura/OneDrive/Desktop/python proj/61/tmp_download"

# Create download folder if it doesn't exist
os.makedirs(download_path, exist_ok=True)

# Download & unzip
print("📥 Downloading...")
api.dataset_download_files(dataset, path=download_path, unzip=True)
print("✅ Downloaded and unzipped.")

# Locate CSV file
csv_path = None
for file in os.listdir(download_path):
    if file.endswith(".csv"):
        csv_path = os.path.join(download_path, file)
        break

if csv_path:
    print(f"📄 Found file: {csv_path}")
    df = pd.read_csv(csv_path)
    print(df.head())

    # Save a clean copy for app use
    cleaned_path = "C:/Users/Noura/OneDrive/Desktop/python proj/61/data/cleaned_stock_data.csv"
    df.to_csv(cleaned_path, index=False)
    print(f"✅ Cleaned data saved to: {cleaned_path}")
else:
    print("❌ CSV not found.")
