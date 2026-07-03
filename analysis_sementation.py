import pandas as pd
import matplotlib.pyplot as plt
import os

## create folder
os.makedirs("Outputs/Q3_Segmentation", exist_ok=True)

## load
merged_df = pd.read_csv("Outputs/merged_df.csv")

## frequent vs infrequent traders

trade_count = (
    merged_df.groupby("Account")
    .size()
    .reset_index(name="Total Trades")
)

median_trades = trade_count["Total Trades"].median()

trade_count["Trader Type"] = trade_count["Total Trades"].apply(
    lambda x: "Frequent Trader"
    if x >= median_trades
    else "Infrequent Trader"
)

print(trade_count.head())

## save to csv
trade_count.to_csv(
    "Outputs/Q3_Segmentation/frequent_vs_infrequent.csv",
    index=False
)

## chart
plt.figure(figsize=(6,4))

trade_count["Trader Type"].value_counts().plot(kind="bar")

plt.title("Frequent vs Infrequent Traders")
plt.xlabel("Trader Type")
plt.ylabel("Number of Traders")

plt.tight_layout()

plt.savefig(
    "Outputs/Q3_Segmentation/frequent_vs_infrequent.png",
    dpi=300
)

plt.show()

##Consistent Winners vs Inconsistent Traders

merged_df["Win"] = merged_df["Closed PnL"] > 0

winner = (
    merged_df.groupby("Account")["Win"]
    .mean()
    .mul(100)
    .reset_index(name="Win Rate (%)")
)

## create segment
winner["Trader Category"] = winner["Win Rate (%)"].apply(
    lambda x: "Consistent Winner"
    if x >= 50
    else "Inconsistent Trader"
)

print(winner.head())

## save to csv
winner.to_csv(
    "Outputs/Q3_Segmentation/consistent_winners.csv",
    index=False
)

## chart
plt.figure(figsize=(6,4))

winner["Trader Category"].value_counts().plot(kind="bar")

plt.title("Consistent vs Inconsistent Traders")
plt.xlabel("Trader Category")
plt.ylabel("Number of Traders")

plt.tight_layout()

plt.savefig(
    "Outputs/Q3_Segmentation/consistent_winners.png",
    dpi=300
)

plt.show()

##High PnL vs Low PnL Traders

total_pnl = (
    merged_df.groupby("Account")["Closed PnL"]
    .sum()
    .reset_index()
)

median_pnl = total_pnl["Closed PnL"].median()

##create segment
total_pnl["PnL Category"] = total_pnl["Closed PnL"].apply(
    lambda x: "High PnL"
    if x >= median_pnl
    else "Low PnL"
)

print(total_pnl.head())

## save to csv
total_pnl.to_csv(
    "Outputs/Q3_Segmentation/high_vs_low_pnl.csv",
    index=False
)

## chart
plt.figure(figsize=(6,4))

total_pnl["PnL Category"].value_counts().plot(kind="bar")

plt.title("High PnL vs Low PnL Traders")
plt.xlabel("PnL Category")
plt.ylabel("Number of Traders")

plt.tight_layout()

plt.savefig(
    "Outputs/Q3_Segmentation/high_vs_low_pnl.png",
    dpi=300
)

plt.show()