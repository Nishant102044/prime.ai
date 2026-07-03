import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Title
st.set_page_config(page_title="Crypto Trading Dashboard", layout="wide")

st.title("📊 Crypto Trader Performance Dashboard")

# Load Dataset
merged_df = pd.read_csv("Outputs/merged_df.csv")

# Sidebar
st.sidebar.title("Filters")

sentiment = st.sidebar.multiselect(
    "Select Market Sentiment",
    merged_df["classification"].unique(),
    default=merged_df["classification"].unique()
)

filtered_df = merged_df[
    merged_df["classification"].isin(sentiment)
]

# ===========================
# KPIs
# ===========================

st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Trades", len(filtered_df))

col2.metric(
    "Total PnL",
    round(filtered_df["Closed PnL"].sum(),2)
)

win_rate = (
    (filtered_df["Closed PnL"] > 0).mean()*100
)

col3.metric(
    "Win Rate %",
    round(win_rate,2)
)

# ===========================
# Average PnL
# ===========================

st.subheader("Average PnL by Sentiment")

pnl = (
    filtered_df.groupby("classification")["Closed PnL"]
    .mean()
)

fig, ax = plt.subplots(figsize=(6,4))

ax.bar(
    pnl.index,
    pnl.values
)

ax.set_xlabel("Sentiment")
ax.set_ylabel("Average PnL")

st.pyplot(fig)

# ===========================
# Trade Frequency
# ===========================

st.subheader("Trade Frequency")

trade_frequency = (
    filtered_df.groupby("classification")
    .size()
)

fig, ax = plt.subplots(figsize=(6,4))

ax.bar(
    trade_frequency.index,
    trade_frequency.values
)

ax.set_xlabel("Sentiment")
ax.set_ylabel("Trades")

st.pyplot(fig)

# ===========================
# Position Size
# ===========================

st.subheader("Average Position Size")

position = (
    filtered_df.groupby("classification")["Size USD"]
    .mean()
)

fig, ax = plt.subplots(figsize=(6,4))

ax.bar(
    position.index,
    position.values
)

ax.set_xlabel("Sentiment")
ax.set_ylabel("Average Size USD")

st.pyplot(fig)

# ===========================
# Long / Short Bias
# ===========================

st.subheader("Long vs Short")

direction = (
    filtered_df[
        filtered_df["Direction"].isin(
            [
                "Open Long",
                "Close Long",
                "Open Short",
                "Close Short"
            ]
        )
    ]["Direction"]
    .value_counts()
)

fig, ax = plt.subplots(figsize=(7,4))

ax.bar(
    direction.index,
    direction.values
)

plt.xticks(rotation=20)

st.pyplot(fig)

# ===========================
# Daily PnL
# ===========================

st.subheader("Daily PnL")

daily = (
    filtered_df.groupby("Date")["Closed PnL"]
    .sum()
)

fig, ax = plt.subplots(figsize=(10,4))

ax.plot(
    daily.index,
    daily.values
)

plt.xticks(rotation=45)

st.pyplot(fig)

# ===========================
# Data Preview
# ===========================

st.subheader("Dataset Preview")

st.dataframe(filtered_df.head(20))