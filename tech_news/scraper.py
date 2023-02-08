# Requisito 1
import requests
from time import sleep
from requests.exceptions import ConnectionError, ReadTimeout
from parsel import Selector


def fetch(url):
    sleep(1)
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
    except (ConnectionError, ReadTimeout):
        return None

    if response.status_code == 200:
        return response.text
    return None


# Requisito 2
def scrape_updates(html_content):
    html = Selector(text=html_content)
    links = html.css("a.cs-overlay-link ::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    html = Selector(text=html_content)
    next_page = html.css("a.next.page-numbers ::attr(href)").get()
    return next_page


# Requisito 4
def scrape_news(html_content):
    html = Selector(text=html_content)
    url = html.css("head > link[rel='canonical'] ::attr(href)").get()
    title = html.css("h1.entry-title ::text").get().strip()
    writer = html.css("a.url.fn.n ::text").get()
    timestamp = html.css("li.meta-date ::text").get()
    reading_time = int(
        html.css("li.meta-reading-time ::text").get().split(" ")[0]
    )
    category = html.css("span.label ::text").get()
    summary = html.css("div.entry-content > p:nth-of-type(1) *::text").getall()

    data = {
        "url": url,
        "title": title,
        "writer": writer,
        "timestamp": timestamp,
        "reading_time": reading_time,
        "summary": "".join(summary).strip(),
        "category": category,
    }
    return data


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    html = fetch("https://blog.betrybe.com/")
    links = scrape_updates(html)
    print(scrape_news(fetch(links[9])))
