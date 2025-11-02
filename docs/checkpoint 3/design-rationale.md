# Design Rationale — Relational Data Visualization

**Team:** Moises’ Team  
**Members:** Luis Arturo Michel Pérez, Oscar Martínez Estévez, Moisés Jesús Carrillo Alonso, Braulio Jesús Pérez Tamayo, Gerardo Hernández Widman, Mario David Hernández Pantoja  
**Project:** Portfolio – CheckPoint 3 (Relational Data Visualization)

---

## 1. Visualization Purpose

The main goal of this practice was to explore **relational data** derived from movies and their shared genres. The visualization choices were made to:

* Represent **relationships** and **influence** among movies.
* Compare different **centrality measures** (degree, closeness, betweenness, PageRank).
* Identify **patterns and correlations** between movie attributes (rating, popularity) and structural network importance.

The following visualizations were designed to balance **statistical clarity** and **structural insight**.

---

## 2. Visualization 1: Distribution of Centrality Metrics

### Purpose

To understand how centrality scores (degree, closeness, betweenness, PageRank) are distributed across all nodes (movies).

### Justification

A **histogram** was chosen because:

* It provides a clear overview of **how many movies fall within certain ranges** of centrality.
* It reveals **skewness** and **outliers**, showing whether influence is concentrated in a few nodes.
* The inclusion of a **mean line** helps quickly identify the typical value of each metric.

### Insights Supported

* Shows that most movies have moderate centrality while a small subset are highly connected.
* Helps detect which centrality metric best differentiates movies in the network.

---

## 3. Visualization 2: Correlation Heatmap

### Purpose

To explore **relationships** between centrality metrics and movie attributes such as rating and popularity.

### Justification

A **correlation heatmap** using a diverging color scale (`coolwarm`) was selected because:

* It visually encodes both **magnitude** and **direction** of correlations.
* The grid layout enables **simultaneous comparison** between all metrics.
* Annotated coefficients provide immediate quantitative interpretation.

### Insights Supported

* Detects if network centrality aligns with audience metrics like rating or popularity.
* Highlights potential dependencies (e.g., whether higher-rated movies tend to be more central).

---

## 4. Visualization 3: Top Movies Comparison (Grouped Bar Chart)

### Purpose

To compare the most central movies according to multiple metrics simultaneously.

### Justification

A **grouped bar chart** was chosen because:

* It enables **direct comparison across different centrality types** for the same movies.
* Bars were **normalized** to allow scale comparability between metrics with different value ranges.
* Compact horizontal grouping helps emphasize **multidimensional performance** (Degree vs PageRank vs Closeness).

### Insights Supported

* Highlights which movies are consistently central across metrics.
* Makes it easier to identify movies that are structurally important but not necessarily popular.
* Reveals that “Steven Universe: The Movie” and “The Dark Knight” exhibit strong network connectivity and influence.

---

## 5. Visualization 4: Scatter Plots (Rating vs Centrality)

### Purpose

To study how **centrality relates to real-world performance indicators** like ratings and popularity.

### Justification

Scatter plots were chosen because:

* They effectively show **relationships between two continuous variables**.
* **Color encoding (popularity)** adds a third dimension, showing how audience attention interacts with structural importance.
* Multiple subplots (one for each centrality type) allow **side-by-side pattern comparison**.

### Insights Supported

* Reveals whether higher-rated or more popular movies tend to occupy more central network positions.
* Provides an intuitive visual connection between **network theory metrics** and **cinematic success**.

---

## 6. Overall Design Choices

### Color Palette

* The **“husl” palette** from Seaborn was used for clarity and diversity.
* Contrasting colors ensure easy metric distinction across figures.
* Neutral backgrounds (via `seaborn-darkgrid`) improve readability of fine-grained patterns.

### Layout and Readability

* Subplot structures (2×2 grids) balance information density and legibility.
* Axis labels, legends, and titles are consistent and descriptive.
* All figures maintain tight layouts to optimize space and avoid overlapping labels.

### Interactivity Consideration

While the visualizations are static, they were structured so that they could be extended into **interactive dashboards** (e.g., with Plotly or Bokeh) for dynamic filtering by genre, rating, or popularity.

---

## 7. Conclusion

Each visualization was selected to represent a **different analytical perspective**:

* **Distributions** → Understand metric variability.
* **Heatmap** → Detect correlations and dependencies.
* **Bar chart** → Compare top nodes across metrics.
* **Scatter plots** → Link network structure to real-world outcomes.

Together, they provide a **holistic understanding** of the movie network—combining statistical, comparative, and relational insights to reveal which films play central roles within the genre-based movie ecosystem.
