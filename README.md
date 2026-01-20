# 📈 Bitcoin Market Sentiment Analysis

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)](https://github.com/paikshal/.-Bitcoin-Market-Sentiment-)

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

*Sample insights from our analysis:*

| Classification | Total PnL ($) | Avg PnL ($) | Win Rate (%) | Assessment |
| :--- | :--- | :--- | :--- | :--- |
| **Extreme Fear** | $739,110 | $34.54 | 37.06% | 🟢 Strong Buy Opportunity |
| **Neutral** | $1,292,920 | $34.31 | 39.70% | 🟡 Moderate Performance |
| **Extreme Greed** | $2,715,171 | $67.89 | 46.49% | 🔴 High Volatility / Selling Zone |

*(Note: Data above is illustrative based on project outputs.)*

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
