import pandas as pd


## load datasets
historical_df = pd.read_csv("historical_data.csv")
fear_greed_df = pd.read_csv("fear_greed_index.csv")

## count no of rows& coloumns
print("Historical Data Shape :", historical_df.shape)
print("Fear & Greed Shape :", fear_greed_df.shape)

## missing values
print("\nMissing Values in Historical Data")

print(historical_df.isnull().sum())

print("\nMissing Values in Fear & Greed Data")

print(fear_greed_df.isnull().sum())

## duplicate values
print("Historical Duplicates :", historical_df.duplicated().sum())

print("Fear & Greed Duplicates :", fear_greed_df.duplicated().sum())

# Convert Historical Timestamp IST to datetime
historical_df["Timestamp IST"] = pd.to_datetime(
    historical_df["Timestamp IST"],
    format="%d-%m-%Y %H:%M"
)

# Convert Fear & Greed Date to datetime
fear_greed_df["Date"] = pd.to_datetime(
    fear_greed_df["Date"],
    errors="coerce"
)

# Extract only Date
historical_df["Date"] = historical_df["Timestamp IST"].dt.date

fear_greed_df["Date"] = fear_greed_df["Date"].dt.date

# Merge both datasets on Date
merged_df = pd.merge(
    historical_df,
    fear_greed_df,
    on="Date",
    how="left"
)

print(merged_df.head())

## check merged
# print(merged_df.shape)
# print(merged_df.head())
# print(merged_df[["Date", "value", "classification"]].head(10))
# print(merged_df.columns)


# ###key metrics
# ##daily pnlper trader

daily_pnl = (
    merged_df.groupby(["Date", "Account"])["Closed PnL"]
    .sum()
    .reset_index()
)
print(daily_pnl.head())

# save to csv
daily_pnl.to_csv(
    "Outputs/daily_pnl_per_account.csv",
    index=False
)

print("Daily PnL saved successfully!")


# ## win rate
merged_df["Win"] = merged_df["Closed PnL"] > 0

win_rate = (
    merged_df.groupby("Account")["Win"]
    .mean()
    .mul(100)
    .reset_index(name="Win Rate (%)")
)

print(win_rate.head())
## save to csv
win_rate.to_csv(
    "Outputs/win_rate.csv",
    index=False
)

print("Win Rate saved successfully!")

# ## average trade size
avg_trade_size = (
    merged_df.groupby("Account")["Size USD"]
    .mean()
    .reset_index(name="Average Trade Size (USD)")
)

print(avg_trade_size.head())

## save to csv
avg_trade_size.to_csv(
    "Outputs/average_trade_size.csv",
    index=False
)

print("Average Trade Size saved successfully!")

## leverage distribution
 # Not calculated because the dataset does not contain a leverage-related column.
leverage_note = pd.DataFrame({
    "Message": [
        "Leverage Distribution could not be calculated because the dataset does not contain a Leverage column. Position Size (Size USD) was analyzed instead to understand trader behavior."
    ]
})

leverage_note.to_csv(
    "Outputs/leverage_distribution.csv",
    index=False
)

print("Leverage note saved successfully!")


## no of trade 
trades_per_day = merged_df.groupby("Date").size().reset_index(name="Total Trades")

print(trades_per_day.head())

# save to csv
trades_per_day.to_csv(
    "Outputs/trades_per_day.csv",
    index=False
)

print("Trades Per Day saved successfully!")

## long short ratio
long_short_ratio = (
    merged_df[
        merged_df["Direction"].isin(
            ["Open Long", "Close Long", "Open Short", "Close Short"]
        )
    ]["Direction"]
    .value_counts(normalize=True)
    .mul(100)
    .reset_index()
)

long_short_ratio.columns = ["Direction", "Percentage"]

print(long_short_ratio)
#save to csv
long_short_ratio.to_csv(
    "Outputs/long_short_ratio.csv",
    index=False
)

print("Long/Short Ratio Saved Successfully!")

# Save merged dataset
merged_df.to_csv("Outputs/merged_df.csv", index=False)

print("Merged dataset saved successfully!")