# Cryptocurrency Spatiotemporal Analysis
### Integrating Financial Volatility and Global Search Interest (2020–2025)

## 1. Project Overview
This project investigates the **spatiotemporal behavior of major cryptocurrencies** by combining financial price data from **Yahoo Finance** with global search interest from **Google Trends**. The goal is to explore how **public attention** and **market volatility** interact across time and geography.

The analysis is divided into two major components:

1. **Temporal Analysis (Part I)** – Statistical exploration of cryptocurrency price dynamics, returns, and volatility over time.
2. **Spatial Analysis (Part II)** – Examination of geographic search interest, highlighting regional patterns and correlations between attention and market behavior.

Through the integration of these dimensions, the study aims to identify **lead–lag relationships**, **volatility clustering**, and **regional influence** in cryptocurrency markets between **October 2020 and October 2025**.

## 2. Data and Methodology

### 2.1 Data Sources
The project integrates three key data sources:

| Source | Description | Frequency | Format |
|--------|--------------|------------|---------|
| **Yahoo Finance** | Historical price data (Open, High, Low, Close, Volume) for Bitcoin, Ethereum, Tether, BNB, and Solana | Daily | CSV |
| **Google Trends** | Search interest for the same cryptocurrencies across ten countries | Weekly | CSV |
| **Natural Earth** | Geographic coordinates and shapefiles for country visualization | Static | GeoJSON/CSV |

### 2.2 Datasets
1. **prices_with_metrics.csv** – Enriched daily price dataset containing returns, logarithmic returns, and rolling volatility (7d, 30d).
2. **trends_enriched.csv** – Weekly Google Trends dataset enriched with ISO codes, geographic coordinates, and regional grouping.
3. **integrated_data.csv** – Merged dataset aligning price and search data on matching dates and countries for spatiotemporal analysis.
4. **country_aggregated.csv** – Country-level summary metrics for comparative studies and heatmaps.

### 2.3 Methodological Framework

#### Part I – Time Series Analysis
- **Stationarity Testing:** Augmented Dickey–Fuller (ADF) tests were used to assess the presence of unit roots in price series.
- **Autocorrelation Analysis:** ACF and PACF plots were applied to returns and squared returns to evaluate volatility clustering.
- **Volatility Modeling:** Rolling window variance and logarithmic returns were employed to quantify short- and long-term market fluctuations.

#### Part II – Spatial Analysis
- **Search Interest Mapping:** Choropleth maps were generated to visualize Google Trends scores per country and over time.
- **Regional Aggregation:** Mean interest levels were compared across geographic regions (Americas, Europe, Asia).
- **Temporal Patterns:** Time series of interest were aligned with volatility metrics to detect synchronized trends.

#### Part III – Spatiotemporal Integration
- **Correlation and Cross-Correlation (CCF):** Evaluated the temporal relationship between search interest and volatility per country.
- **Lead–Lag Interpretation:** Negative lags indicate public attention preceding volatility; positive lags suggest the opposite.

## 3. Results Summary

### 3.1 Temporal Findings
- Cryptocurrency prices exhibited **high volatility and strong autocorrelation** in squared returns, consistent with GARCH-type behavior.
- Bitcoin and Ethereum displayed **persistent volatility clustering**, while stablecoins like Tether showed minimal fluctuations.
- The log returns confirmed **non-stationarity in prices** but stationarity in returns, supporting the weak form of the Efficient Market Hypothesis.

### 3.2 Spatial Findings
- Global search interest varied significantly: **Asia and the Americas** demonstrated the highest engagement levels.
- Countries such as **Brazil, the United States, and India** consistently ranked among the top in crypto-related search intensity.
- Spatial visualization revealed **temporal diffusion of interest**, with peaks aligning with major market events and price rallies.

### 3.3 Integrated Insights
- Cross-correlation analysis showed **negative lags in several markets**, indicating that rising search interest often **preceded volatility spikes**.
- This relationship was strongest for Bitcoin in the U.S. and Ethereum in India, suggesting early predictive signals embedded in public attention data.

## 4. Setup Instructions

### 4.1 Requirements
```bash
Python ≥ 3.10
pandas, numpy, matplotlib, seaborn, statsmodels
plotly, geopandas, pytrends, yfinance
```

### 4.2 Installation
```bash
git clone https://github.com/yourusername/crypto-spatiotemporal-analysis.git
cd crypto-spatiotemporal-analysis
pip install -r requirements.txt
```

### 4.3 Data Preparation
```bash
# 1. Geographic data
python geodata.py

# 2. Google Trends data (3–5 hours)
python trends.py

# 3. Yahoo Finance prices (2–3 minutes)
python yahoot.py

# 4. Data integration and aggregation
python integrate_data.py
```

All generated files (`*.csv`, `*.geojson`) will appear in the `/data` directory.

## 5. Usage Guide

### 5.1 Running the Analysis
Open and execute the notebook `p2.ipynb`.
It reproduces all visualizations and statistical analyses, including:
- ACF/PACF and volatility clustering plots.
- Correlation matrices between returns and interest.
- Interactive choropleth maps using Plotly.
- Cross-correlation (CCF) graphs for lead–lag exploration.

### 5.2 Interpreting Outputs
| Output | Description |
|--------|--------------|
| **ACF & PACF plots** | Measure dependence over time; reveal persistence and clustering. |
| **Choropleth maps** | Show relative search intensity globally. |
| **CCF plots** | Identify whether public attention anticipates or follows volatility. |
| **Country summary table** | Aggregated statistics useful for cross-country comparisons. |

## 6. Conclusion
This project provides a unified framework for **quantifying the interaction between public interest and cryptocurrency market volatility**. By merging temporal and spatial data, it bridges behavioral and financial dimensions of crypto economics.

The findings support that **search attention can act as a leading indicator** of volatility in specific regions, especially for highly liquid assets. Such results emphasize the value of integrating **digital behavioral data** with traditional financial indicators for predictive analytics and market understanding.

## 7. License and Attribution
This work is distributed for **academic and educational purposes** only.
Please cite the respective data providers:
- Yahoo Finance (market data)
- Google Trends (search data)
- Natural Earth (geographic data)

**Members of the Team Project:**
David
Oscar
Moi
Braulio
Gerardo
Luis 

**Last Updated:** October 2025  
