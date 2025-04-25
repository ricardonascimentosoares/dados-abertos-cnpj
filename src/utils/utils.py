import os
import tempfile
import shutil

def get_subfolder_paths(folder_path):
  """
  Returns a list of all subfolder names within a given folder (Pythonic way).

  Args:
    folder_path: The path to the folder.

  Returns:
    A list of strings, where each string is the name of a subfolder.
    Returns an empty list if the folder doesn't exist or has no subfolders.
  """
  if not os.path.isdir(folder_path):
    return []
  return [
      os.path.join(folder_path, item)
      for item in os.listdir(folder_path)
      if os.path.isdir(os.path.join(folder_path, item))
  ]


def remove_extracted_files(extract_dir):
    """Remove the extracted files after processing."""
    print(f"Removing extracted files from {extract_dir}...")
    try:
        shutil.rmtree(extract_dir)
        print(f"Successfully removed extracted files from {extract_dir}.")
    except Exception as e:
        print(f"Error removing extracted files: {e}")

def convert_to_utf8(src_file):
    """Convert a file from windows-1252 to utf-8 encoding and return the path to the new file."""
    temp_fd, temp_path = tempfile.mkstemp(suffix='.utf8.csv')
    os.close(temp_fd)
    with open(src_file, 'r', encoding='windows-1252', errors='replace') as fin, \
         open(temp_path, 'w', encoding='utf-8', errors='replace') as fout:
        shutil.copyfileobj(fin, fout)
    return temp_path