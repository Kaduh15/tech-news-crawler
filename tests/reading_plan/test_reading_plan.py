from unittest.mock import patch
from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
import pytest


mock_file = [
    {
        "title": "news 01",
        "reading_time": 4,
    },
    {
        "title": "news 02",
        "reading_time": 3,
    },
    {
        "title": "news 03",
        "reading_time": 10,
    },
    {
        "title": "news 04",
        "reading_time": 15,
    },
    {
        "title": "news 05",
        "reading_time": 12,
    },
]


def test_reading_plan_group_news():
    pass

    with patch(
        "tech_news.analyzer.reading_plan.find_news", return_value=mock_file
    ):
        data = ReadingPlanService.group_news_for_available_time(10)

        assert data["readable"] == [
            {
                "unfilled_time": 3,
                "chosen_news": [("news 01", 4), ("news 02", 3)],
            },
            {
                "unfilled_time": 0,
                "chosen_news": [("news 03", 10)],
            },
        ]

        assert data["unreadable"] == [
            ("news 04", 15),
            ("news 05", 12),
        ]

    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        return ReadingPlanService.group_news_for_available_time(0)
