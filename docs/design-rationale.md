# Design Rationale: Visualization and Analytical Choices

## 1. Purpose of Visualization
The visualizations in this project were designed to **translate complex temporal and spatial dynamics** into intuitive visual evidence. Each plot, map, or graph was chosen not only for statistical accuracy but for its capacity to tell a coherent story about **market volatility and public behavior**.

---

## 2. Visualization Principles
1. **Clarity over Complexity:** Each figure isolates one analytical dimension (time, volatility, geography) to avoid visual overload.  
2. **Comparability:** Consistent color scales and time intervals ensure meaningful cross-crypto and cross-country comparisons.  
3. **Narrative Flow:** Visuals follow a logical sequence — from time series, to geographic patterns, to integrated analyses — mirroring the cognitive path of discovery.  
4. **Evidence Integrity:** Only statistically grounded representations (e.g., rolling metrics, correlations) are visualized to avoid misleading interpretations.

---

## 3. Key Visualization Types and Rationale

### 3.1 Time Series and Volatility Plots
- **Purpose:** Display price evolution, returns, and volatility clustering.  
- **Rationale:** Line plots with rolling averages clearly illustrate persistence and cyclicality in volatility.  
- **Insight Supported:** Volatility is not random — periods of instability endure over time.

### 3.2 ACF and PACF Plots
- **Purpose:** Examine autocorrelation structure of prices and returns.  
- **Rationale:** Statistical visual tools like ACF/PACF communicate the depth of dependency in the time series.  
- **Insight Supported:** Confirms the weak efficiency of crypto markets and memory in volatility processes.

### 3.3 Choropleth Maps
- **Purpose:** Visualize geographic distribution of search interest by country.  
- **Rationale:** Choropleths provide intuitive spatial storytelling, transforming numerical data into regional context.  
- **Insight Supported:** Reveals geographic asymmetry in adoption and attention levels.

### 3.4 Regional Time Series
- **Purpose:** Track search interest over time by global region.  
- **Rationale:** Multi-line regional plots emphasize cultural and economic differences in adoption trends.  
- **Insight Supported:** Confirms that public interest growth is heterogeneous across continents.

### 3.5 Cross-Correlation (CCF) Graphs
- **Purpose:** Detect temporal relationships between public attention and volatility.  
- **Rationale:** CCF plots visualize directionality — showing whether attention precedes or follows market activity.  
- **Insight Supported:** Identifies behavioral precursors to financial volatility.

---

## 4. Color and Aesthetic Design

- **Color Palette:** A **neutral base (grays)** with **accent colors (blue–orange)** to differentiate crypto assets and maintain readability.  
- **Spatial Visuals:** Sequential color scales (light-to-dark gradients) communicate magnitude of search interest effectively.  
- **Temporal Visuals:** Muted tones reduce noise, emphasizing patterns rather than decoration.  
- **Interactive Elements:** In Plotly maps and time series, hover interactivity allows contextual exploration without cluttering static visuals.

---

## 5. Storytelling Through Design
The visualization choices were guided by the principle that **design should enhance insight, not decoration**. Each visual serves a rhetorical function:  
- **Time series** show uncertainty.  
- **Maps** reveal inequality of adoption.  
- **Cross-correlations** expose behavioral causality.  

Together, they construct a narrative arc — from randomness, to persistence, to prediction — mirroring the intellectual journey of the research.

---

**Members of the Team Project:**
David
Oscar
Moi
Braulio
Gerardo
Luis 

**Last Updated:** October 2025  
