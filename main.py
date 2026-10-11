import requests
from bs4 import BeautifulSoup

url = input("URL: ").strip()

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=10,
)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

for title in soup.find_all(["h1", "h2", "h3"]):
    text = title.get_text(" ", strip=True)
    if text:
        print("-", text)
