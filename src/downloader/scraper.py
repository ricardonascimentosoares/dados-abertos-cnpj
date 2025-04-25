import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_download_links(url):
    """Scrape the webpage and retrieve all .zip file links."""
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.endswith('.zip'):
            links.append(urljoin(url, href))
    return links