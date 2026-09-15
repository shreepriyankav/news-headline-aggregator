import pandas as pd


def transform_headlines(articles):
    records = []

    for article in articles:
        records.append({
            "title": article.get("title"),
            "source": article.get("source", {}).get("name"),
            "category": "General",
            "published_at": article.get("publishedAt"),
            "url": article.get("url")
        })

    df = pd.DataFrame(records)

    # Remove headlines without a title
    df = df.dropna(subset=["title"])

    # Remove duplicate headlines
    df = df.drop_duplicates(subset=["title"])

    # Clean text
    df["title"] = df["title"].str.strip()
    df["source"] = df["source"].fillna("Unknown").str.strip()

    # Convert published time
    df["published_at"] = pd.to_datetime(
        df["published_at"],
        errors="coerce"
    )

    return df


if __name__ == "__main__":
    print("Transform module ready.")
