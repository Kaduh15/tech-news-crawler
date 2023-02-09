from tech_news.database import find_news


# Requisito 7
def search_by_title(title):
    news_data = find_news()
    news_filtered = []
    for news in news_data:
        title_news = news["title"].lower()
        has_title = title.lower() in title_news
        if has_title:
            news_filtered.append((news['title'], news['url']))
    return news_filtered


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    news_data = find_news()
    news_filtered = []
    for news in news_data:
        category_news = news["category"].lower()
        has_category = category.lower() in category_news
        if has_category:
            news_filtered.append((news['title'], news['url']))
    return news_filtered
