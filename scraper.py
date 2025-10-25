import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import time
def get_headers():
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    }
def test_website_access(url, site_name):
    try:
        response = requests.get(url, headers=get_headers(), timeout=10)
        if response.status_code == 200:
            return True, response
        else:
            return False, None
    except:
        return False, None
def scrape_bbc():
    articles = []
    url = "https://www.bbc.com/news"
    success, response = test_website_access(url, "BBC News")
    if not success:
        return articles
    soup = BeautifulSoup(response.content, 'html5lib')
    selectors = [
        'a[data-testid="internal-link"]',
        '.gs-c-promo-heading',
        '.ssrcss-1m1x8nf-PromoLink'
    ]
    for sel in selectors:
        elems = soup.select(sel)
        if elems and len(elems) > 3:
            for el in elems[:10]:
                title = el.get_text().strip()
                if title and len(title) > 15:
                    link = el.get('href', '#')
                    if link.startswith('/'):
                        link = f"https://www.bbc.com{link}"
                    articles.append({
                        'title': title,
                        'journalist': 'BBC Correspondent',
                        'outlet': 'BBC News',
                        'section': 'General',
                        'date': datetime.now().strftime('%Y-%m-%d'),
                        'url': link,
                        'content_preview': title[:80] + '...' if len(title) > 80 else title
                    })
            break
    return articles

def scrape_ap():
    articles = []
    url = "https://apnews.com/"
    success, response = test_website_access(url, "Associated Press")
    if not success:
        return articles

    soup = BeautifulSoup(response.content, 'html5lib')
    headlines = soup.find_all(['h1', 'h2', 'h3'])
    for h in headlines[:12]:
        title = h.get_text().strip()
        if title and len(title) > 20 and not any(word in title.lower() for word in ['subscribe', 'login', 'sign up']):
            articles.append({
                'title': title,
                'journalist': 'AP Staff',
                'outlet': 'Associated Press',
                'section': 'General',
                'date': datetime.now().strftime('%Y-%m-%d'),
                'url': '#',
                'content_preview': title[:70] + '...' if len(title) > 70 else title
            })
    return articles

def scrape_techcrunch():
    articles = []
    url = "https://techcrunch.com/"
    success, response = test_website_access(url, "TechCrunch")
    if not success:
        return articles

    soup = BeautifulSoup(response.content, 'html5lib')
    links = soup.find_all('a', href=re.compile(r'/\d{4}/\d{2}/\d{2}/'))
    for link in links[:8]:
        title = link.get_text().strip()
        if title and len(title) > 10:
            full_url = link.get('href', '#')
            if full_url and not full_url.startswith('http'):
                full_url = f"https://techcrunch.com{full_url}"
            articles.append({
                'title': title,
                'journalist': 'TechCrunch Writer',
                'outlet': 'TechCrunch',
                'section': 'Technology',
                'date': datetime.now().strftime('%Y-%m-%d'),
                'url': full_url,
                'content_preview': title[:60] + '...' if len(title) > 60 else title
            })
    return articles

def scrape_theverge():
    articles = []
    url = "https://www.theverge.com/"
    success, response = test_website_access(url, "The Verge")
    if not success:
        return articles

    soup = BeautifulSoup(response.content, 'html5lib')
    h2h3 = soup.find_all(['h2','h3'])
    for art in h2h3[:6]:
        title = art.get_text().strip()
        if title and len(title) > 15:
            link_elem = art.find('a')
            link = link_elem.get('href', '#') if link_elem else '#'
            if link and not link.startswith('http'):
                link = f"https://www.theverge.com{link}"
            articles.append({
                'title': title,
                'journalist': 'The Verge Editor',
                'outlet': 'The Verge',
                'section': 'Technology',
                'date': datetime.now().strftime('%Y-%m-%d'),
                'url': link,
                'content_preview': title[:65] + '...' if len(title) > 65 else title
            })
    return articles

# --------- Main Scraper Function ---------
def scrape_all_sites():
    all_articles = []

    for func in [scrape_bbc, scrape_ap, scrape_techcrunch, scrape_theverge]:
        all_articles.extend(func())
        time.sleep(1)  # polite scraping

    # Remove duplicates by normalized title
    seen_titles = set()
    unique_articles = []
    for art in all_articles:
        key = art['title'].lower().strip()[:50]
        if key not in seen_titles:
            seen_titles.add(key)
            unique_articles.append(art)

    return unique_articles

# --------- Test Function ---------
if __name__ == "__main__":
    articles = scrape_all_sites()
    for a in articles[:5]:
        print(a)
