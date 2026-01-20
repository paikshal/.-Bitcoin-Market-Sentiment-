
## 🚀 Overview

The **Bitcoin Market Sentiment Analysis** project investigates the relationship between market sentiment (measured by the Fear & Greed Index) and crypto trading performance. By correlating historical trading data with sentiment classifications, this tool uncovers hidden patterns to help refine trading strategies.

Does "Extreme Fear" offer the best buying opportunities? Is "Extreme Greed" a signal to sell? This analysis answers these questions with data-backed insights.

## 📊 Key Features

- **Sentiment Correlation**: Merges trading history with daily Fear & Greed Index values.
- **Performance Metrics**: Calculates key metrics for each sentiment category:
  - **Total PnL (Profit and Loss)**
  - **Average PnL per Trade**
  - **Win Rate %**
  - **Risk Velocity**
  - **Trade Volume**
- **Visualizations**: Insightful charts generated using `matplotlib` and `seaborn` to visualize performance trends.
- **Data-Driven Insights**: Outputs a detailed `Final_Analysis.csv` report summarizing trader performance across different market moods.

## 📂 Project Structure

```bash
├── csv_files/
│   └── Final_Analysis.csv    # Consolidated analysis results
├── notebook_1.ipynb          # Main Jupyter Notebook with analysis logic
├── fear_greed_index.csv      # Source data: Fear & Greed Index history
├── historical_data.csv       # Source data: Historical trading records
└── README.md                 # Project documentation
```

## 🛠️ Installation & Usage

1.  **Clone the Repository**
    ```bash
    git clone git@github.com:paikshal/.-Bitcoin-Market-Sentiment-.git
    cd .-Bitcoin-Market-Sentiment-
    ```

2.  **Install Dependencies**
    Ensure you have Python installed, then run:
    ```bash
    pip install pandas matplotlib seaborn
    ```

3.  **Run the Analysis**
    Open the Jupyter Notebook to run the analysis step-by-step:
    ```bash
    jupyter notebook notebook_1.ipynb
    ```

## 📈 Analysis Highlights

Based on our historical data analysis, here are the key performance metrics across different market sentiments:

| Classification | Total PnL ($) | Avg PnL ($) | Win Rate (%) | Risk Velocity | Assessment |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Extreme Greed** | $2,715,171 | **$67.89** | **46.49%** | 766.83 | 🚀 **Highest Efficiency** (Best Win Rate & Avg PnL) |
| **Fear** | **$3,357,155** | $54.29 | 42.08% | 935.36 | 💰 **Highest Volume** (Most Overall Profit) |
| **Greed** | $2,150,129 | $42.74 | 38.48% | 1116.03 | ⚠️ High Risk / Lower Win Rate |
| **Neutral** | $1,292,920 | $34.31 | 39.70% | 517.12 | ⚖️ Stable but Average Returns |
| **Extreme Fear** | $739,110 | $34.54 | 37.06% | 1136.06 | 🛑 **Lowest Performance** (Lowest Win Rate & Returns) |

### 💡 Key Takeaways
1.  **Contrary to Popular Belief**: "Extreme Greed" periods actually yielded the **highest win rate (46.5%)** and **highest average profit per trade ($67.89)**, suggesting strong momentum trading opportunities.
2.  **Volume vs. Efficiency**: While "Fear" sentiment generated the most **total profit ($3.35M)** due to higher trade volume, it was less efficient per trade compared to "Extreme Greed".
3.  **Caution in Extreme Fear**: "Extreme Fear" proved to be the least profitable market state, with the lowest win rate (37%) and high risk velocity, contradicting the "buy the dip" strategy for this specific dataset.

## 🤝 Contributing

Contributions are welcome! If you have ideas for new metrics or better visualizations, feel free to open an issue or submit a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---
<p align="center">
  Built with ❤️ by Paikshal Prajapati
</p>
