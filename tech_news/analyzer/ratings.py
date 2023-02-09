# Requisito 10
from collections import Counter
from tech_news.database import find_news


def top_5_categories():

    data = find_news()
    categories = [news["category"] for news in data]
    count_categories = Counter(categories).most_common(5)
    sorted_categories = sorted(
        count_categories, key=lambda category: (-category[1], category[0])
    )

    return [category[0] for category in sorted_categories]
