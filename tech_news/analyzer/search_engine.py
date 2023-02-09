from datetime import datetime
from tech_news.database import find_news
# from tech_news.scraper import get_tech_news


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
    list_news = find_news()
    if len(date.split('-')[-1]) == 4:
        format_date = datetime.strptime(date, '%d-%m-%Y')
    else:
        format_date = datetime.strptime(date, '%Y-%m-%d')

    news_filtered = []
    for news in list_news:
        date_news = datetime.strptime(news['timestamp'], '%d/%m/%Y').date()
        if format_date == date_news:
            news_filtered.append((news['title'], news['url']))
    return news_filtered


# Requisito 9
def search_by_category(category):
    return search_advanced_news("category", category)


if __name__ == '__main__':
    search_by_date("03-02-2023")
