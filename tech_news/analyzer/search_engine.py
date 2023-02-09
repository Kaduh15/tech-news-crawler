from tech_news.database import find_news


def search_advanced_news(search: str, content: str):
    news_data = find_news()
    news_filtered = []
    for news in news_data:
        content_search = news[search].lower()
        has_content = content.lower() in content_search
        if has_content:
            news_filtered.append((news["title"], news["url"]))
    return news_filtered


# Requisito 7
def search_by_title(title):
    return search_advanced_news('title', title)


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    return search_advanced_news("category", category)
