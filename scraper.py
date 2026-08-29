# Simple demo script using requests & BeautifulSoup
import requests
from bs4 import BeautifulSoup

def fetch_trending():
    url = "https://news.ycombinator.com/" # High traffic developer site
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    titles = soup.find_all('span', class_='titleline')
    for i, title in enumerate(titles[:5], 1):
        print(f"{i}. {title.text}")

if __name__ == "__main__":
    fetch_trending()
