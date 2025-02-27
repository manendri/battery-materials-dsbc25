import os
import requests
import tarfile
import zipfile

# Dataset URLs 
DATASETS = {
    # "QMOF": "",
    "CoRE_MOF": "https://zenodo.org/records/3370144/files/2019-07-01-ASR-internal-overlap-clean_9146.csv",   
    "ARC_MOF": "https://zenodo.org/records/13891643/files/geometric_properties.csv"  
    # "EC_MOF": ""
}

# Parent folder to store downloaded datasets
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

def download_file(url, dataset_name, filename):
    """Download a file from a URL and save it locally in the dataset's folder."""
    dataset_folder = os.path.join(DATA_DIR, dataset_name)
    os.makedirs(dataset_folder, exist_ok=True)  # Ensure dataset folder exists
    filepath = os.path.join(dataset_folder, filename)

    if os.path.exists(filepath):
        print(f"{filename} already exists in {dataset_folder}. Skipping download.")
        return filepath

    print(f"Downloading {filename} to {dataset_folder}...")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Saved: {filepath}")
        return filepath
    else:
        print(f"Failed to download {filename}. Check URL.")
        return None

def extract_file(filepath, dataset_name):
    """Extract tar.gz or zip files inside the respective dataset folder."""
    dataset_folder = os.path.dirname(filepath)  # Extract inside the dataset's folder

    if filepath.endswith(".tar.gz"):
        print(f"Extracting {filepath}...")
        with tarfile.open(filepath, "r:gz") as tar:
            tar.extractall(dataset_folder)
        print(f"Extracted contents to {dataset_folder}/")

    elif filepath.endswith(".zip"):
        print(f"Extracting {filepath}...")
        with zipfile.ZipFile(filepath, "r") as zip_ref:
            zip_ref.extractall(dataset_folder)
        print(f"Extracted contents to {dataset_folder}/")

# Download and extract each dataset
for dataset_name, url in DATASETS.items():
    file_name = url.split("/")[-1]  # Extract filename from URL
    file_path = download_file(url, dataset_name, file_name)

    # Extract if it's an archive file
    if file_path and (file_path.endswith(".tar.gz") or file_path.endswith(".zip")):
        extract_file(file_path, dataset_name)
