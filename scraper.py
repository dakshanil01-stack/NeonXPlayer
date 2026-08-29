import requests
from bs4 import BeautifulSoup
import json

def fetch_trending():
    url = "https://news.ycombinator.com/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    titles = soup.find_all('span', class_='titleline')
    data = []

    for i, title in enumerate(titles[:10], 1):
        a_tag = title.find('a')
        data.append({
            "id": i,
            "title": a_tag.text,
            "url": a_tag['href']
        })
    
    # Save to JSON file
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
        
    print("Data saved to data.json successfully!")

if __name__ == "__main__":
    fetch_trending()
