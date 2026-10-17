import requests
import trafilatura
import re

url = "https://techcrunch.com/2026/10/16/replit-is-no-longer-working-with-anthropic-ceo-says/"
headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/130.0.0.0 Safari/537.36"
        ),
        "Accept": (
            "text/html,application/xhtml+xml,"
            "application/xml;q=0.9,*/*;q=0.8"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }
response = requests.get(
    url=url,
    headers=headers,
    timeout=15
)
html = response.text
extracted = trafilatura.extract(
    html,
    include_comments=False,
    include_tables=False
)
print(extracted.strip())

if extracted and len(extracted.strip())>200:
    cleaned = re.sub(r'\s+',' ',extracted)
    
print("\n\n\n\n----\n\n\n\n",cleaned)