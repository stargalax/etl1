import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.title("Marketing Campaign Dashboard")

# Fetch campaigns
campaigns = requests.get(f"{API_URL}/campaigns").json()

df = pd.DataFrame(campaigns)
st.write(f"📊 There are currently {df.shape[0]} campaigns in the database.")

# Ensure numeric columns are numeric
for col in ["impressions", "clicks", "conversions", "cost", "ctr", "roi"]:
    df[col] = pd.to_numeric(df[col])

st.subheader("All Campaigns Data")
st.dataframe(df)


# Summary metrics
summary = requests.get(f"{API_URL}/campaigns/summary").json()
st.subheader("Summary Metrics")
st.json(summary)


# 1️⃣ Top 5 Campaigns by ROI
st.subheader("Top 5 Campaigns by ROI")
top_roi = df.sort_values(by="roi", ascending=False).head(5)
st.table(top_roi[["campaign_name", "roi"]])

# 2️⃣ Campaigns with CTR > 2%
st.subheader("Campaigns with CTR > 2%")
high_ctr = df[df["ctr"] > 2]
st.table(high_ctr[["campaign_name", "ctr"]])

# 3️⃣ Conversion Rate per Campaign
st.subheader("Conversion Rate per Campaign")
df["conversion_rate"] = df["conversions"] / df["clicks"]
st.bar_chart(df.set_index("campaign_name")["conversion_rate"])

# 4️⃣ Total Spend per Campaign
st.subheader("Cost per Campaign")
st.bar_chart(df.set_index("campaign_name")["cost"])

# 5️⃣ CTR vs ROI Scatter Plot
st.subheader("CTR vs ROI")
st.scatter_chart(df[["ctr", "roi"]])
