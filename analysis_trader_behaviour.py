import pandas as pd
import matplotlib.pyplot as plt
import os

# Create Output Folder
os.makedirs("Outputs/Q2_Trader_Behaviour", exist_ok=True)

# Load Merged Dataset
merged_df = pd.read_csv("Outputs/merged_df.csv")

print(merged_df.head())

##average position size
position_size = (
    merged_df.groupby("classification")["Size USD"]
    .mean()
    .reset_index(name="Average Position Size (USD)")
)

print(position_size)
## save to csv

position_size.to_csv(
    "Outputs/Q2_Trader_Behaviour/position_size.csv",
    index=False
)

print("Position Size CSV Saved Successfully!")

## plot chart
plt.figure(figsize=(7,5))

plt.bar(
    position_size["classification"],
    position_size["Average Position Size (USD)"]
)

plt.title("Average Position Size by Market Sentiment")
plt.xlabel("Market Sentiment")
plt.ylabel("Average Position Size (USD)")

plt.tight_layout()

plt.savefig(
    "Outputs/Q2_Trader_Behaviour/position_size.png",
    dpi=300
)

plt.show()

## long short bias

long_short = (
    merged_df[
        merged_df["Direction"].isin(
            ["Open Long","Close Long","Open Short","Close Short"]
        )
    ]
    .groupby(["classification","Direction"])
    .size()
    .unstack(fill_value=0)
)

print(long_short)

## save to csv
long_short.to_csv(
    "Outputs/Q2_Trader_Behaviour/long_short_bias.csv"
)

### chart
plt.figure(figsize=(8,5))

long_short.plot(kind="bar")

plt.title("Long vs Short Bias by Market Sentiment")
plt.xlabel("Market Sentiment")
plt.ylabel("Number of Trades")

plt.tight_layout()

plt.savefig(
    "Outputs/Q2_Trader_Behaviour/long_short_bias.png",
    dpi=300
)

plt.show()

## leverage 
leverage_note = pd.DataFrame({
    "Message": [
        "Leverage analysis could not be performed because the dataset does not contain a leverage column. Position Size (Size USD) was analyzed instead to understand trader behavior."
        ""
    ]
})

leverage_note.to_csv(
    "Outputs/Q2_Trader_Behaviour/leverage_analysis.csv",
    index=False
)

## trade frequency

trade_frequency = (
    merged_df.groupby("classification")
    .size()
    .reset_index(name="Number of Trades")
)

print(trade_frequency)

## save to csv

trade_frequency.to_csv(
    "Outputs/Q2_Trader_Behaviour/trade_frequency.csv",
    index=False
)

print("Trade Frequency CSV Saved Successfully!")

## bar chart
plt.figure(figsize=(7,5))

plt.bar(
    trade_frequency["classification"],
    trade_frequency["Number of Trades"]
)

plt.title("Trade Frequency by Market Sentiment")
plt.xlabel("Market Sentiment")
plt.ylabel("Number of Trades")

plt.tight_layout()

plt.savefig(
    "Outputs/Q2_Trader_Behaviour/trade_frequency.png",
    dpi=300
)

plt.show()