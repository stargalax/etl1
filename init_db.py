import sqlite3

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

initial_data = [
    (1, "Holiday Promo", 10000, 500, 50, 200, 500/10000, 50/200),
    (2, "Spring Sale", 15000, 600, 75, 300, 600/15000, 75/300),
    (3, "Summer Blast", 20000, 800, 120, 400, 800/20000, 120/400),
    (4, "Winter Discount", 12000, 450, 40, 180, 450/12000, 40/180),
    (5, "Back to School", 18000, 700, 90, 350, 700/18000, 90/350),
    (6, "Flash Sale", 25000, 900, 130, 500, 900/25000, 130/500),
    (7, "Black Friday", 30000, 1200, 200, 800, 1200/30000, 200/800),
    (8, "Cyber Monday", 28000, 1100, 180, 750, 1100/28000, 180/750),
    (9, "Valentine Offer", 15000, 600, 80, 300, 600/15000, 80/300),
    (10, "Easter Promo", 14000, 550, 70, 280, 550/14000, 70/280),
    (11, "Summer Clearance", 22000, 850, 140, 450, 850/22000, 140/450),
    (12, "New Year Blast", 32000, 1300, 210, 850, 1300/32000, 210/850),
    (13, "Autumn Sale", 17000, 650, 85, 330, 650/17000, 85/330),
    (14, "Spring Clearance", 16000, 620, 78, 310, 620/16000, 78/310),
    (15, "Holiday Special", 20000, 800, 120, 400, 800/20000, 120/400),
    (16, "Weekend Flash", 18000, 700, 95, 350, 700/18000, 95/350),
    (17, "Mega Discount", 24000, 950, 150, 480, 950/24000, 150/480),
    (18, "Spring Fest", 15000, 600, 80, 300, 600/15000, 80/300),
    (19, "Summer Sale", 21000, 870, 130, 420, 870/21000, 130/420),
    (20, "Winter Wonderland", 19000, 730, 110, 380, 730/19000, 110/380),
    (21, "Holiday Bonanza", 30000, 1200, 200, 800, 1200/30000, 200/800),
    (22, "Black Friday Special", 32000, 1350, 220, 900, 1350/32000, 220/900),
    (23, "Cyber Sale", 28000, 1100, 180, 750, 1100/28000, 180/750),
    (24, "Valentine Discount", 16000, 640, 85, 320, 640/16000, 85/320),
    (25, "Easter Blast", 15000, 600, 78, 300, 600/15000, 78/300),
    (26, "Summer Clearance 2", 23000, 880, 140, 450, 880/23000, 140/450),
    (27, "New Year Special", 33000, 1400, 220, 900, 1400/33000, 220/900),
    (28, "Autumn Fest", 18000, 680, 90, 340, 680/18000, 90/340),
    (29, "Spring Blast", 17000, 650, 85, 320, 650/17000, 85/320),
    (30, "Holiday Offer", 21000, 820, 130, 420, 820/21000, 130/420),
    (31, "Weekend Sale", 19000, 720, 110, 380, 720/19000, 110/380),
    (32, "Mega Fest", 25000, 950, 150, 480, 950/25000, 150/480),
    (33, "Spring Promo", 16000, 620, 80, 310, 620/16000, 80/310),
    (34, "Summer Discount", 22000, 870, 130, 420, 870/22000, 130/420),
    (35, "Winter Blast", 20000, 750, 120, 400, 750/20000, 120/400),
    (36, "Holiday Sale 2", 31000, 1250, 210, 850, 1250/31000, 210/850),
    (37, "Black Friday Blast", 33000, 1400, 220, 900, 1400/33000, 220/900),
    (38, "Cyber Monday Sale", 29000, 1150, 190, 780, 1150/29000, 190/780),
    (39, "Valentine Special", 17000, 680, 90, 340, 680/17000, 90/340),
    (40, "Easter Offer", 16000, 640, 85, 320, 640/16000, 85/320),
    (41, "Summer Promo 2", 24000, 950, 150, 480, 950/24000, 150/480),
    (42, "New Year Offer", 34000, 1450, 230, 920, 1450/34000, 230/920),
    (43, "Autumn Special", 19000, 730, 110, 380, 730/19000, 110/380),
    (44, "Spring Sale 2", 18000, 680, 95, 340, 680/18000, 95/340),
    (45, "Holiday Promo 3", 22000, 880, 140, 450, 880/22000, 140/450),
    (46, "Weekend Blast", 20000, 750, 120, 400, 750/20000, 120/400),
    (47, "Mega Discount 2", 26000, 980, 160, 500, 980/26000, 160/500),
    (48, "Spring Fest 2", 17000, 650, 85, 320, 650/17000, 85/320),
    (49, "Summer Sale 2", 23000, 900, 140, 450, 900/23000, 140/450),
    (50, "Winter Wonderland 2", 20000, 760, 120, 400, 760/20000, 120/400)
]

# Insert initial data
cursor.executemany("""
    INSERT OR IGNORE INTO campaign
    (campaign_id, campaign_name, impressions, clicks, conversions, cost, ctr, roi)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", initial_data)

conn.commit()
print("Database initialized with sample data.")
conn.close()
