import pandas as pd
import matplotlib.pyplot as plt
import os

## create folders
os.makedirs("Outputs/Q1_Performance_Analysis", exist_ok=True)

## load dataset
merged_df = pd.read_csv("Outputs/merged_df.csv")

print(merged_df.head())

## average pnl by segment
pnl_analysis = (
    merged_df.groupby("classification")["Closed PnL"]
    .agg(
        Total_PnL="sum",
        Average_PnL="mean",
        Number_of_Trades="count"
    )
    .reset_index()
)

print(pnl_analysis)

## save to csv

pnl_analysis.to_csv(
    "Outputs/Q1_Performance_Analysis/pnl_analysis.csv",
    index=False
)

## chart average pnl
plt.figure(figsize=(6,4))

plt.bar(
    pnl_analysis["classification"],
    pnl_analysis["Average_PnL"]
)

plt.title("Average PnL by Market Sentiment")
plt.xlabel("Market Sentiment")
plt.ylabel("Average Closed PnL")

plt.tight_layout()

## save to png
plt.savefig(
    "Outputs/Q1_Performance_Analysis/average_pnl.png",
    dpi=300
)

plt.show()

### win rate
merged_df["Win"] = merged_df["Closed PnL"] > 0

win_rate = (
    merged_df.groupby("classification")["Win"]
    .mean()
    .mul(100)
    .reset_index(name="Win Rate (%)")
)

print(win_rate)

## save to csv
win_rate.to_csv(
    "Outputs/Q1_Performance_Analysis/win_rate.csv",
    index=False
)

## chart win rate
plt.figure(figsize=(6,4))

plt.bar(
    win_rate["classification"],
    win_rate["Win Rate (%)"]
)

plt.title("Win Rate by Market Sentiment")
plt.xlabel("Market Sentiment")
plt.ylabel("Win Rate (%)")

plt.tight_layout()

#save to png
plt.savefig(
    "Outputs/Q1_Performance_Analysis/win_rate.png",
    dpi=300
)

plt.show()

## drow down proxy
drawdown = (
    merged_df[merged_df["Closed PnL"] < 0]
    .groupby("classification")["Closed PnL"]
    .sum()
    .abs()
    .reset_index(name="Drawdown Proxy")
)

print(drawdown)

## save to csv
drawdown.to_csv(
    "Outputs/Q1_Performance_Analysis/drawdown_proxy.csv",
    index=False
)
## save to png

plt.figure(figsize=(6,4))

plt.bar(
    drawdown["classification"],
    drawdown["Drawdown Proxy"]
)

plt.title("Drawdown Proxy by Market Sentiment")
plt.xlabel("Market Sentiment")
plt.ylabel("Drawdown Proxy")

plt.tight_layout()

plt.savefig(
    "Outputs/Q1_Performance_Analysis/drawdown_proxy.png",
    dpi=300
)

plt.show()

