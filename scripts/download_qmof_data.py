import json
import requests
import zipfile
from pathlib import Path

# Set the article ID for QMOF database
ARTICLE_ID = "13147324"

# Figshare API Base URL
BASE_URL = "https://api.figshare.com/v2"

# Get file metadata for the QMOF dataset
response = requests.get(f"{BASE_URL}/articles/{ARTICLE_ID}/files")
file_metadata = response.json()

# Create a folder to store the dataset
DATASET_DIR = Path("data/QMOF")
DATASET_DIR.mkdir(parents=True, exist_ok=True)

# Download each file in the article
for file in file_metadata:
    file_id = file["id"]
    file_name = file["name"]
    download_url = file["download_url"]

    print(f"Downloading {file_name}...")
    file_path = DATASET_DIR / file_name
    file_response = requests.get(download_url)

    # Save the file
    with open(file_path, "wb") as f:
        f.write(file_response.content)

    print(f"Saved {file_name} to {file_path}")

    # If the file is a zip, extract it
    if file_name.endswith(".zip"):
        print(f"Extracting {file_name}...")
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(DATASET_DIR)
        print(f"Extracted contents of {file_name} to {DATASET_DIR}")

        # Optional: Delete the zip file after extraction
        file_path.unlink()
        print(f"Deleted {file_name} after extraction.")

print("All QMOF files downloaded and processed successfully!")
