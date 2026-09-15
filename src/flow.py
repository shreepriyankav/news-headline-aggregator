from prefect import flow, task
from prefect.logging import get_run_logger

from extract import fetch_headlines
from transform import transform_headlines
from load import create_connection, load_headlines


@task(
    name="Extract News Headlines",
    retries=3,
    retry_delay_seconds=5
)
def extract_task():
    logger = get_run_logger()

    logger.info("📥 Extracting news headlines...")

    articles = fetch_headlines()

    logger.info(f"✅ Extracted {len(articles)} articles")

    return articles


@task(
    name="Transform Headlines",
    retries=2,
    retry_delay_seconds=2
)
def transform_task(articles):
    logger = get_run_logger()

    logger.info("🔄 Transforming headlines...")

    df = transform_headlines(articles)

    logger.info(f"✅ Transformed {len(df)} articles")

    return df


@task(
    name="Load Headlines to MySQL",
    retries=3,
    retry_delay_seconds=5
)
def load_task(df):
    logger = get_run_logger()

    logger.info("💾 Loading headlines into MySQL...")

    connection = create_connection()

    try:
        load_headlines(connection, df)
    finally:
        connection.close()

    logger.info("✅ MySQL load completed")


@flow(name="news-headline-aggregator")
def news_pipeline():

    logger = get_run_logger()

    logger.info("=" * 60)
    logger.info("🚀 NEWS HEADLINE AGGREGATOR - PREFECT FLOW")
    logger.info("=" * 60)

    # Step 1 - Extract
    articles = extract_task()

    # Step 2 - Transform
    df = transform_task(articles)

    # Step 3 - Load
    load_task(df)

    logger.info("=" * 60)
    logger.info("🎉 PREFECT FLOW COMPLETED!")
    logger.info("=" * 60)


if __name__ == "__main__":
    news_pipeline()
