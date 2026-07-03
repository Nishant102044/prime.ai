# Crypto Trader Behavior Analysis using Fear & Greed Index

## Project Overview

This project analyzes cryptocurrency traders' behavior by combining historical trading data with the Crypto Fear & Greed Index. The objective is to understand how market sentiment influences trader performance and trading behavior.

---

## Project Objectives

* Clean and prepare both datasets.
* Merge trading data with Fear & Greed Index.
* Calculate key trading metrics.
* Analyze trader behavior under different market sentiments.
* Generate actionable trading insights.
* Build a simple Streamlit dashboard.

---

## Technologies Used

* Python
* Pandas
* Matplotlib
* Streamlit

---

## Project Structure

* **Part_A_Data_Preparation.py** – Data cleaning and merging.
* **Part_B_Key_Metrics.py** – Calculates trading metrics.
* **Part_C_Analysis.py** – Performance and behavioral analysis.
* **dashboard.py** – Interactive Streamlit dashboard.

---

## How to Run

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run analysis

```bash
python Part_A_Data_Preparation.py
python Part_B_Key_Metrics.py
python Part_C_Analysis.py
```

### Run Dashboard

```bash
streamlit run dashboard.py
```

---

# Project Summary

## Methodology

Two datasets were loaded and cleaned using Pandas. Timestamp fields were converted into datetime format and both datasets were merged on the Date column. Missing values and duplicates were checked before performing the analysis.

Key metrics such as Daily PnL, Win Rate, Average Trade Size, Trades per Day, and Long/Short Ratio were calculated. Since the dataset did not contain a leverage column, leverage-based analysis was not performed.

Trader performance and behavior were compared across different market sentiment categories (Fear, Greed, and Neutral). Traders were also segmented into Frequent vs Infrequent Traders and Consistent Winners vs Inconsistent Traders.

## Key Insights

* Trading performance varies across different market sentiment conditions.
* Trading activity changes depending on market sentiment, with differences observed in trade frequency and average position size.
* Frequent traders and consistent winners show different behavioral patterns compared to other trader groups.

## Strategy Recommendations

1. During Fear periods, traders should reduce position sizes and avoid excessive trading to manage downside risk.

2. During Greed periods, traders may increase trading activity if supported by favorable performance metrics while maintaining disciplined risk management.

## Conclusion

This project demonstrates how market sentiment influences trader behavior and performance. The analysis can help traders and analysts develop more informed, data-driven trading strategies.


## Output

The Outputs folder contains:

* Clean merged dataset
* CSV summary tables
* Charts (.png)
* Segmentation results

---

## Author

Nishant
