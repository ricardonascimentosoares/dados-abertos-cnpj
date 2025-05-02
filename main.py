import os
from concurrent.futures import ThreadPoolExecutor
from src.config.paths import BASE_URL, DOWNLOAD_DIR, EXTRACT_DIR
from src.downloader.scraper import get_download_links
from src.downloader.file_downloader import download_file, extract_zip
from src.etl import processor
from src.utils.utils import remove_extracted_files, get_subfolder_paths

def process_download(link):
    """Download and extract a single file."""
    print(f"Downloading {link}...")
    zip_file_path = download_file(link, DOWNLOAD_DIR)
    
    file_name = os.path.basename(link)
    category = ''.join(filter(str.isalpha, file_name.split('.')[0])).lower()
    category_dir = os.path.join(EXTRACT_DIR, category)
    os.makedirs(category_dir, exist_ok=True)
    
    print(f"Extracting {zip_file_path} to {category_dir}...")
    extract_zip(zip_file_path, category_dir)
    return category_dir


def main():
    # Step 1: Download and extract files
    print("Starting download process...")
    download_links = get_download_links(BASE_URL)
    print(f"Found {len(download_links)} files to download.")

    with ThreadPoolExecutor(max_workers=10) as executor:
        list(executor.map(process_download, download_links))

    # Step 2: Process extracted files
    print("\nStarting ETL process...")
    processor.create_aux_tables()

    for folder_path in get_subfolder_paths(EXTRACT_DIR):
        folder_name = os.path.basename(folder_path)
        processor.process_folder(folder_name, folder_path)

    # Step 3: Remove extracted files
    remove_extracted_files(EXTRACT_DIR)

    print("All processes completed successfully.")
    print("Check the output directory for results.")

if __name__ == "__main__":
    main()