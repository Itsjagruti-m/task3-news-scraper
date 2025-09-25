import requests
from bs4 import BeautifulSoup


def fetch_headlines(url="https://www.bbc.com/news"):
    """Fetch top headlines from the given news site."""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print("❌ Error fetching page:", e)
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    # Adjust tag/class depending on site structure
    headlines = []
    for h in soup.find_all("h2"):
        text = h.get_text(strip=True)
        if text and text not in headlines:
            headlines.append(text)

    return headlines[:10]  # limit to top 10


def save_headlines(headlines, filename="headlines.txt"):
    """Save headlines to a text file."""
    with open(filename, "w", encoding="utf-8") as f:
        for line in headlines:
            f.write(line + "\n")
    print(f"✅ Headlines saved to {filename}")


if __name__ == "__main__":
    url = "https://www.bbc.com/news"
    headlines = fetch_headlines(url)
    if headlines:
        save_headlines(headlines)
    else:
        print("⚠️ No headlines found.")
