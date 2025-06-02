import requests
from bs4 import BeautifulSoup

def smart_scrape(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(res.text, "html.parser")

    # Try to get titles, headlines, paragraphs
    headlines = soup.find_all(["h1", "h2", "h3"], limit=20)
    paragraphs = soup.find_all("p", limit=20)

    data = []
    #
    for h in headlines:
        data.append("📰 " + h.get_text(strip=True))
    for p in paragraphs:
        data.append("📄 " + p.get_text(strip=True))


    return "\n".join(data)
