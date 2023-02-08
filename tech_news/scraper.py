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
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    html = fetch("https://blog.betrybe.com/")
    scrape_updates(html)
