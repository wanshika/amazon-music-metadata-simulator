import psycopg2
import pandas as pd
from config import DB_CONFIG

def create_tables():
    print("📥 Creating tables from schema.sql...")
    with open("database/schema.sql", "r") as f:
        schema = f.read()

    with psycopg2.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            cur.execute(schema)
            print("✅ Tables created successfully.")

def load_csv_to_table(csv_file, table_name):
    print(f"📂 Loading data from {csv_file} into {table_name}...")
    df = pd.read_csv(csv_file)
    with psycopg2.connect(**DB_CONFIG) as conn:
        cur = conn.cursor()
        for _, row in df.iterrows():
            cols = ', '.join(row.index)
            placeholders = ', '.join(['%s'] * len(row))
            values = tuple(row.values)
            sql = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
            try:
                cur.execute(sql, values)
            except Exception as e:
                print(f"❌ Error inserting into {table_name}: {e}")
        conn.commit()
        print(f"✅ {len(df)} records inserted into {table_name}.")

if __name__ == "__main__":
    print("🚀 Starting ingestion process...")
    create_tables()
    load_csv_to_table("data/artists.csv", "artists")
    load_csv_to_table("data/tracks.csv", "tracks")
    load_csv_to_table("data/rights.csv", "rights")
    print("✅ All done!")
