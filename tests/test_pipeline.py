from src.transform import transform_headlines


def test_transform_headlines():
    articles = [
        {
            "title": "Test News",
            "source": {"name": "Test Source"},
            "publishedAt": "2026-09-15T10:00:00Z",
            "url": "https://example.com/test-news"
        }
    ]

    df = transform_headlines(articles)

    assert len(df) == 1
    assert df.iloc[0]["title"] == "Test News"
    assert df.iloc[0]["source"] == "Test Source"
    assert df.iloc[0]["category"] == "General"
