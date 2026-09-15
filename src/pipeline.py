from extract import fetch_headlines
from transform import transform_headlines
from load import create_connection, load_headlines


def run_pipeline():
    print("=" * 60)
    print("🚀 NEWS HEADLINE AGGREGATOR PIPELINE")
    print("=" * 60)

    # Extract
    print("\n📥 Step 1: Fetching headlines...")
    articles = fetch_headlines()
    print(f"✅ Fetched {len(articles)} articles")

    # Transform
    print("\n🔄 Step 2: Transforming data...")
    df = transform_headlines(articles)
    print(f"✅ Transformed {len(df)} articles")

    # Load
    print("\n💾 Step 3: Loading into MySQL...")
    connection = create_connection()

    try:
        load_headlines(connection, df)
    finally:
        connection.close()

    print("\n" + "=" * 60)
    print("🎉 PIPELINE COMPLETED SUCCESSFULLY!")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()

