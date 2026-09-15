import os
import hashlib

import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def create_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return connection


def generate_url_hash(url):
    return hashlib.sha256(url.encode("utf-8")).hexdigest()


def load_headlines(connection, df):
    query = """
        INSERT INTO headlines
        (title, source, category, published_at, url, url_hash)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    cursor = connection.cursor()

    inserted = 0
    skipped = 0

    for _, row in df.iterrows():

        url_hash = generate_url_hash(row["url"])

        try:
            cursor.execute(
                query,
                (
                    row["title"],
                    row["source"],
                    row["category"],
                    row["published_at"].to_pydatetime()
                    if hasattr(row["published_at"], "to_pydatetime")
                    else row["published_at"],
                    row["url"],
                    url_hash
                )
            )

            inserted += 1

        except mysql.connector.IntegrityError:
            skipped += 1

    connection.commit()
    cursor.close()

    print(f"✅ New headlines inserted: {inserted}")
    print(f"⏭️ Duplicate headlines skipped: {skipped}")


if __name__ == "__main__":
    connection = create_connection()

    print("✅ MySQL connection successful!")

    connection.close()

    print("🔒 MySQL connection closed.")
