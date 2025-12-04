import sqlite3
import random
import time

# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect("campaign.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS campaign (
    campaign_id INTEGER PRIMARY KEY,
    campaign_name TEXT,
    impressions INTEGER,
    clicks INTEGER,
    conversions INTEGER,
    cost REAL,
    ctr REAL,
    roi REAL
)
""")
conn.commit()

print("Starting ETL simulation...")

while True:
    # Generate random campaign data
    campaign_id = random.randint(1000, 9999)
    campaign_name = f"Promo_{campaign_id}"
    impressions = random.randint(5000, 20000)
    clicks = random.randint(100, 1000)
    conversions = random.randint(10, 100)
    cost = random.randint(100, 500)
    ctr = clicks / impressions
    roi = conversions / cost

    # Insert into database
    cursor.execute("""
        INSERT INTO campaign
        (campaign_id, campaign_name, impressions, clicks, conversions, cost, ctr, roi)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (campaign_id, campaign_name, impressions, clicks, conversions, cost, ctr, roi))
    conn.commit()

    print(f"Inserted new campaign: {campaign_name}")
    time.sleep(60)  # Insert every 60 seconds
