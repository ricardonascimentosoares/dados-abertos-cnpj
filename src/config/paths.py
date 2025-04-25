import os
import datetime
import requests

# Base directories
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output")
DOWNLOAD_DIR = os.path.join(OUTPUT_DIR, "downloads")
EXTRACT_DIR = os.path.join(OUTPUT_DIR, "extracted")
DUCKDB_FILE = os.path.join(OUTPUT_DIR, "dados_abertos_cnpj.db")

# Create directories if they don't exist
os.makedirs(DOWNLOAD_DIR, exist_ok=True)
os.makedirs(EXTRACT_DIR, exist_ok=True)

def get_latest_available_base_url():
    """Find the most recent available CNPJ data URL."""
    base_url_template = "https://arquivos.receitafederal.gov.br/dados/cnpj/dados_abertos_cnpj/{year}-{month:02d}/"
    today = datetime.date.today()
    year = today.year
    month = today.month

    # Try up to 24 months back
    for _ in range(24):
        url = base_url_template.format(year=year, month=month)
        try:
            response = requests.head(url, timeout=5)
            if response.status_code == 200:
                return url
        except Exception:
            pass
        # Go to previous month
        month -= 1
        if month == 0:
            month = 12
            year -= 1
    raise RuntimeError("No available CNPJ data URL found in the last 24 months.")

# URLs
BASE_URL = get_latest_available_base_url()