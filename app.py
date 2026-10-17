"""
import requests
import trafilatura


def extract_article(url: str) -> str:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        if response.status_code == 403:
            return (
                "ACCESS_DENIED: The website returned HTTP 403. "
                "Use an authorized alternative source."
            )

        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "")

        if "text/html" not in content_type.lower():
            return "UNSUPPORTED_CONTENT: The URL did not return HTML."

        article_text = trafilatura.extract(
            response.text,
            include_comments=False,
            include_tables=False
        )

        if not article_text:
            return "EXTRACTION_FAILED: No article text was found."

        return article_text

    except requests.Timeout:
        return "TIMEOUT: The website took too long to respond."

    except requests.RequestException as exc:
        return f"REQUEST_FAILED: {exc}"


url = (
    "https://www.artificialintelligence-news.com/news/"
    "ai-big-data-expo-europe-sets-out-the-next-steps-for-enterprise-ai/"
)
url = "https://www.artificialintelligence-news.com/news/ai-big-data-expo-europe-sets-out-the-next-steps-for-enterprise-ai/"
print(extract_article(url))



mport requests
import trafilatura

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def create_session():
    session = requests.Session()

    retry_strategy = Retry(
        total=3,
        connect=3,
        read=2,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"],
        respect_retry_after_header=True,
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)

    session.mount("https://", adapter)
    session.mount("http://", adapter)

    session.headers.update({
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
    })

    return session


def extract_article(url: str) -> str:
    session = create_session()

    response = session.get(
        url,
        timeout=(5, 20),
    )

    print("Status code:", response.status_code)

    response.raise_for_status()

    article = trafilatura.extract(response.text)

    if not article:
        raise ValueError(
            "The webpage loaded, but article extraction failed."
        )


    return article


url = (
    "https://www.artificialintelligence-news.com/news/"
    "ai-big-data-expo-europe-sets-out-the-next-steps-for-enterprise-ai/"
)
url = "https://www.reddit.com/r/corporate/comments/1x6pptu/i_feel_like_i_stole_500k_from_my_company/"

try:
    article = extract_article(url)
    print("\n--- Extracted Article ---\n")
    print(article)

except requests.exceptions.RequestException as e:
    print("Request failed:", repr(e))

except ValueError as e:
    print("Extraction failed:", e)

import requests

url = (
    "https://www.reddit.com/r/corporate/comments/"
    "1x6pptu/i_feel_like_i_stole_500k_from_my_company/.json"
)

headers = {
    "User-Agent": "python:reddit-post-reader:1.0 (personal project)"
}

response = requests.get(
    url,
    headers=headers,
    timeout=(5, 20),
)

print("Status code:", response.status_code)
response.raise_for_status()

data = response.json()

post = data[0]["data"]["children"][0]["data"]

title = post.get("title", "")
body = post.get("selftext", "")

print("Title:", title)
print("\nPost body:\n", body)"""

import requests
import trafilatura

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def create_session():
    session = requests.Session()

    retry_strategy = Retry(
        total=3,
        connect=3,
        read=2,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"],
        respect_retry_after_header=True,
    )

    adapter = HTTPAdapter(max_retries=retry_strategy)

    session.mount("https://", adapter)
    session.mount("http://", adapter)

    session.headers.update({
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
    })

    return session


def extract_article(url: str) -> str:
    session = create_session()

    response = session.get(
        url,
        timeout=(5, 20),
    )

    print("Status code:", response.status_code)

    response.raise_for_status()

    article = trafilatura.extract(response.text)

    if not article:
        raise ValueError(
            "The webpage loaded, but article extraction failed."
        )


    return article


"""url = (
    "https://www.artificialintelligence-news.com/news/"
    "ai-big-data-expo-europe-sets-out-the-next-steps-for-enterprise-ai/
)"""
url = "https://www.ndtv.com/topic/visakhapatnam"


try:
    article = extract_article(url)
    print("\n--- Extracted Article ---\n")
    print(article)

except requests.exceptions.RequestException as e:
    print("Request failed:", repr(e))

except ValueError as e:
    print("Extraction failed:", e)


