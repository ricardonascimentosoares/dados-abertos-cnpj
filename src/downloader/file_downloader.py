import os
import requests
from tqdm import tqdm
import zipfile

def download_file(url, dest_folder):
    """Download a file from a URL to the specified folder with a progress bar."""
    local_filename = os.path.join(dest_folder, os.path.basename(url))
    
    # Check if file exists
    if os.path.exists(local_filename):
        print(f"File {local_filename} already exists.")
        return local_filename

    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))
        with open(local_filename, 'wb') as f, tqdm(
            desc=f"Downloading {os.path.basename(url)}",
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as progress_bar:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                progress_bar.update(len(chunk))
    return local_filename

def extract_zip(file_path, extract_to):
    """Extract a zip file to the specified folder."""
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)