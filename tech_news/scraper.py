# Requisito 1
from time import sleep
import requests
from requests.exceptions import ConnectionError, ReadTimeout


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
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
