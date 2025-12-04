
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from typing import List, Dict

app = FastAPI(title="Marketing Campaign ETL API")
DB_PATH = "campaign.db"

class Campaign(BaseModel):
    campaign_id: int
    campaign_name: str
    impressions: int
    clicks: int
    conversions: int
    cost: float
    ctr: float
    roi: float

def get_data() -> List[Campaign]:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM campaign ORDER BY campaign_id DESC")
    rows = cursor.fetchall()
    conn.close()
    
    data = []
    for r in rows:
        data.append(Campaign(
            campaign_id=r[0],
            campaign_name=r[1],
            impressions=r[2],
            clicks=r[3],
            conversions=r[4],
            cost=r[5],
            ctr=r[6],
            roi=r[7]
        ))
    return data

# @app.get("/campaigns", response_model=List[Campaign])
# def read_campaigns():
#     return get_data()

# @app.get("/campaigns/{campaign_id}", response_model=Campaign)
# def read_campaign(campaign_id: int):
#     all_data = get_data()
#     campaign = next((c for c in all_data if c.campaign_id == campaign_id), None)
#     if not campaign:
#         raise HTTPException(status_code=404, detail="Campaign not found")
#     return campaign

# @app.get("/campaigns/summary", response_model=Dict)
# def campaign_summary():
#     data = get_data()
#     total_impressions = sum(c.impressions for c in data)
#     total_clicks = sum(c.clicks for c in data)
#     total_conversions = sum(c.conversions for c in data)
#     total_cost = sum(c.cost for c in data)
#     ctr = (total_clicks / total_impressions * 100) if total_impressions else 0
#     roi = (sum(c.roi for c in data)/len(data)) if data else 0
@app.get("/campaigns", response_model=List[Campaign])
def read_campaigns():
    return get_data()

@app.get("/campaigns/summary", response_model=Dict)
def campaign_summary():
    data = get_data()
    total_impressions = sum(c.impressions for c in data)
    total_clicks = sum(c.clicks for c in data)
    total_conversions = sum(c.conversions for c in data)
    total_cost = sum(c.cost for c in data)
    ctr = (total_clicks / total_impressions * 100) if total_impressions else 0
    roi = (sum(c.roi for c in data)/len(data)) if data else 0

    return {
        "total_campaigns": len(data),
        "total_impressions": total_impressions,
        "total_clicks": total_clicks,
        "total_conversions": total_conversions,
        "total_cost": total_cost,
        "average_ctr": round(ctr, 2),
        "average_roi": round(roi, 2)
    }

@app.get("/campaigns/{campaign_id}", response_model=Campaign)
def read_campaign(campaign_id: int):
    all_data = get_data()
    campaign = next((c for c in all_data if c.campaign_id == campaign_id), None)
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return campaign

    return {
        "total_campaigns": len(data),
        "total_impressions": total_impressions,
        "total_clicks": total_clicks,
        "total_conversions": total_conversions,
        "total_cost": total_cost,
        "average_ctr": round(ctr, 2),
        "average_roi": round(roi, 2)
    }
