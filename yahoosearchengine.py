import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote, urlparse, parse_qs

def extract_real_url(yahoo_url: str) -> str:
    # Example: https://r.search.yahoo.com/.../RU=https%3a%2f%2fexample.com/...
    parsed = urlparse(yahoo_url)
    if "r.search.yahoo.com" in parsed.netloc:
        qs = parse_qs(parsed.path)
        # Pull the true URL from the path (Yahoo encodes real URL after /RU=...)
        try:
            ru_part = yahoo_url.split("/RU=")[1].split("/RK=")[0]
            return unquote(ru_part)
        except IndexError:
            return yahoo_url
    return yahoo_url

def yahoo_search(query: str) -> str:
    url = f"https://search.yahoo.com/search?p={query}"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        )
    }

    res = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(res.text, "html.parser")
    results = []

    for link in soup.find_all("a", href=True):
        href = link["href"]
        text = link.get_text(strip=True)
        if (
            "r.search.yahoo.com" in href and
            text and len(text.split()) > 3  # Only keep real titles, not "Privacy" etc.
        ):
            real_url = extract_real_url(href)
            results.append(f"🔗 {text}\n{real_url}\n")

    return "\n".join(results[0:6]) if results else "❌ No results found."

# Test
if __name__ == "__main__":
    print(yahoo_search(""))
