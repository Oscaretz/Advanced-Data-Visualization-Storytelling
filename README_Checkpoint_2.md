# Checkpoint 2: Hierarchical Data Visualization

**Advanced Data Visualization & Storytelling**  
**Phase 1: Portfolio Checkpoint 2**

---

## 📋 Project Overview

This project implements comprehensive hierarchical data visualization techniques to analyze complex multilevel datasets. The primary focus is on creating interactive and static visualizations that reveal patterns, relationships, and insights within hierarchical structures across three distinct domains: global demographics, organizational structure, and budget allocation.

### 🎯 Primary Use Case: Strategic Decision Support

**End User:** Marco Antonelli, CEO of Terra Cotta Foods (TCF)  
**Business Context:** Global expansion strategy into Latin America and Asia  
**Objective:** Enable data-driven decisions on market selection, supplier diversification, and resource allocation

---

## 👥 Team

**Moises' Team**
- Luis Arturo Michel Perez
- Oscar Martinez Estevez
- Moises Jesus Carrillo Alonso
- Braulio Jesus Perez Tamayo
- Gerardo Hernandez Widman
- Mario David Hernandez Pantoja

---

## 📊 Datasets

### 1. Global Demographics Dataset
- **Source:** UN Data (195 countries)
- **File:** `gdp_population_and_continent_un_195_countries.csv`
- **Variables:**
  - Country name
  - Continent
  - Population
  - GDP (total and per capita)
- **Purpose:** Market assessment and expansion strategy analysis

### 2. Organizational Structure Dataset
- **Source:** Synthetic tech company data
- **File:** `empresas_tech.csv`
- **Variables:**
  - Company hierarchy (department → team → role)
  - Employee count per level
  - Organizational units
- **Purpose:** Resource distribution and team structure analysis

### 3. Budget Allocation Dataset
- **Source:** Synthetic organizational budget
- **File:** `budget_data.csv`
- **Variables:**
  - Department budgets
  - Project allocations
  - Investment priorities
- **Purpose:** Financial planning and resource optimization

---

## 🎨 Visualization Techniques

### 1. **Treemap Analysis**
- **Purpose:** Display proportional relationships while preserving hierarchy
- **Implementation:** 
  - Static treemaps using `squarify` and `matplotlib`
  - Interactive treemaps using `plotly`
- **Use Case:** World population distribution by continent and country
- **Key Insight:** Asia dominates with 58.9% of global population

### 2. **Dendrogram (Hierarchical Clustering)**
- **Purpose:** Reveal similarity patterns and natural groupings
- **Implementation:** 
  - Ward linkage method using `scipy.cluster.hierarchy`
  - Feature scaling with `sklearn.preprocessing`
- **Use Case:** Country clustering based on economic indicators
- **Key Insight:** 5 distinct economic clusters identified

### 3. **Sunburst Chart**
- **Purpose:** Radial visualization of nested hierarchies
- **Implementation:** Interactive charts using `plotly`
- **Use Case:** Organizational structure visualization
- **Key Insight:** Engineering represents 36% of workforce

### 4. **Circular Treemap**
- **Purpose:** Circular representation of proportional hierarchies
- **Implementation:** Custom circular layouts with `plotly`
- **Use Case:** Budget distribution across departments
- **Key Insight:** 50% of budget allocated to engineering

### 5. **Comparative Analysis**
- **Purpose:** Evaluate visualization effectiveness across techniques
- **Implementation:** Side-by-side comparisons with quantitative metrics
- **Key Insight:** Each technique optimized for specific analytical scenarios

---

## 🏗️ Project Structure

```
Advanced-Data-Visualization-Storytelling/
│
├── data_files/
│   └── checkpoint2/
│       ├── gdp_population_and_continent_un_195_countries.csv
│       ├── empresas_tech.csv
│       └── budget_data.csv
│
├── notebooks/
│   ├── 01_hierarchical_analysis.ipynb.ipynb
│   └── .ipynb_checkpoints/
│
├── dashboards/
│   └── technical-dashboard/
│       ├── streamlit_app.py
│       └── pages/
│           ├── 1_Treemaps.py
│           ├── 2_Dendrogram.py
│           ├── 3_Sunburst.py
│           ├── 4_Circular_Treemap.py
│           ├── 5_Comparison.py
│           └── 6_Quantitative_Analysis.py
│
├── processing_scripts/
│   └── checkpoint 2/
│       ├── paises.py          # Country data processing
│       ├── companys.py         # Company data processing
│       └── budget.py           # Budget data processing
│
├── visualizations/
│   └── hierarchical/
│       └── 01_hierarchical_analysis.ipynb_files/
│
├── docs/
│   └── checkpoint 2/
│       ├── who-what-how-framework.md
│       ├── big-ideas.md
│       ├── design-rationale.md
│       └── storyboards/
│           └── phase1_hierarchical_storyboard.pdf
│
├── requirements.txt
└── README_Checkpoint_2.md (this file)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Jupyter Notebook or JupyterLab
- Modern web browser (for Streamlit dashboard)

### Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd Advanced-Data-Visualization-Storytelling
```

2. **Create a virtual environment (recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

### Required Libraries

```
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
plotly>=5.11.0
squarify>=0.4.3
scipy>=1.9.0
scikit-learn>=1.1.0
streamlit>=1.25.0
jupyter>=1.0.0
```

---

## 📖 Usage

### 1. Data Processing

Process raw data files before analysis:

```bash
# Process country/GDP data
python processing_scripts/checkpoint\ 2/paises.py

# Process organizational data
python processing_scripts/checkpoint\ 2/companys.py

# Process budget data
python processing_scripts/checkpoint\ 2/budget.py
```

### 2. Jupyter Notebook Analysis

Open and run the main analysis notebook:

```bash
jupyter notebook notebooks/01_hierarchical_analysis.ipynb.ipynb
```

**Notebook Sections:**
1. Library imports and configuration
2. Data loading and preprocessing
3. Exploratory Data Analysis (EDA)
4. Treemap visualizations (static & interactive)
5. Dendrogram clustering analysis
6. Sunburst organizational charts
7. Circular treemap budget analysis
8. Comparative technique evaluation
9. Quantitative insights and conclusions

### 3. Interactive Dashboard

Launch the Streamlit technical dashboard:

```bash
cd dashboards/technical-dashboard
streamlit run streamlit_app.py
```

**Dashboard Features:**
- **Page 1 - Treemaps:** Interactive population and GDP visualization
- **Page 2 - Dendrogram:** Hierarchical clustering exploration
- **Page 3 - Sunburst:** Organizational structure navigation
- **Page 4 - Circular Treemap:** Budget allocation analysis
- **Page 5 - Comparison:** Side-by-side technique comparison
- **Page 6 - Quantitative Analysis:** Statistical insights and metrics

**Access:** Open browser at `http://localhost:8501`

### Visualization Effectiveness

| Technique | Best For | Limitation |
|-----------|----------|------------|
| Treemap | Proportional relationships, medium datasets | Deep hierarchy readability |
| Dendrogram | Similarity analysis, clustering | Lacks quantitative scale |
| Sunburst | Multilevel navigation, radial hierarchy | Label overlap in dense data |
| Circular Treemap | Budget/resource allocation | Complex interpretation |

---

## 📚 Documentation

### Core Documents

1. **[Storyboard](docs/checkpoint%202/storyboards/phase1_hierarchical_storyboard.pdf)**
   - Visual narrative for Marco Antonelli (CEO, Terra Cotta Foods)
   - Decision journey from data to strategic action
   - Design specifications and interaction flows

2. **[Who-What-How Framework](docs/checkpoint%202/who-what-how-framework.md)**
   - Audience analysis (Marco Antonelli profile)
   - Action objectives (market selection, resource allocation)
   - Data strategy (hierarchical visualization approach)

3. **[Big Ideas](docs/checkpoint%202/big-ideas.md)**
   - Core insights from analysis
   - Key messages for stakeholders
   - Strategic implications

4. **[Design Rationale](docs/checkpoint%202/design-rationale.md)**
   - Justification for visualization choices
   - Color scheme and typography decisions
   - Interaction design principles

---

## 🎯 Learning Objectives Achieved

✅ **Hierarchical Visualization Mastery**
- Implemented 4+ distinct hierarchical techniques
- Understood strengths and limitations of each approach

✅ **Data Analysis Skills**
- Performed hierarchical clustering (Ward method)
- Calculated GDP per capita and population metrics
- Conducted comparative statistical analysis

✅ **Technical Implementation**
- Python data science stack proficiency
- Interactive visualization with Plotly
- Dashboard development with Streamlit

✅ **Business Communication**
- Translated technical insights into business value
- Created executive-level storyboards
- Designed decision-support visualizations

✅ **Strategic Thinking**
- Connected data patterns to business decisions
- Evaluated market opportunities quantitatively
- Recommended resource allocation strategies

---

## 🛠️ Technical Specifications

### Visualization Parameters

**Treemap:**
- Layout algorithm: Squarified
- Size encoding: Population or GDP
- Color encoding: GDP per capita (gradient)
- Interactivity: Hover tooltips, click drill-down

**Dendrogram:**
- Linkage method: Ward (minimum variance)
- Distance metric: Euclidean
- Feature scaling: StandardScaler
- Optimal clusters: 5 (elbow method)

**Sunburst:**
- Radial layout: Center-to-edge hierarchy
- Size encoding: Employee count
- Color scheme: Categorical per department
- Interactivity: Click zoom, breadcrumb navigation

**Circular Treemap:**
- Packing algorithm: Circle packing
- Size encoding: Budget amount
- Color scheme: Department-based
- Hierarchy: 2-3 levels

---

## 🔄 Workflow

```mermaid
graph LR
A[Raw Data] --> B[Processing Scripts]
B --> C[Clean Data]
C --> D[Jupyter Analysis]
D --> E[Visualizations]
E --> F[Dashboard]
F --> G[Business Insights]
G --> H[Strategic Decisions]
```

---

## 📊 Data Quality Notes

- **Coverage:** 195 countries with complete GDP and population data
- **Source:** UN official statistics (reliable, standardized)
- **Synthetic Data:** Company and budget datasets are illustrative
- **Preprocessing:** Missing values handled, outliers preserved for analysis
- **Validation:** Cross-checked continent assignments and calculations

---

## 🎨 Design Philosophy

### Principles Applied

1. **Clarity Over Complexity**
   - Minimal cognitive load
   - Intuitive visual encoding
   - Clear hierarchical relationships

2. **Executive-Ready**
   - Boardroom-quality aesthetics
   - Professional color schemes
   - Export-friendly formats

3. **Actionable Insights**
   - Direct path from visualization to decision
   - Quantified metrics visible
   - Comparative context provided

4. **Interactive Exploration**
   - User-driven drill-down
   - Multi-level filtering
   - Responsive hover states

---

## 📝 Assignment Compliance

### Deliverables Checklist

- [x] **Documentation**
  - [x] phase1-hierarchical-storyboard.pdf
  - [x] who-what-how-framework.md
  - [x] big-ideas.md
  - [x] design-rationale.md

- [x] **Data Files**
  - [x] gdp_population_and_continent_un_195_countries.csv
  - [x] empresas_tech.csv
  - [x] budget_data.csv

- [x] **Visualizations**
  - [x] Static treemaps
  - [x] Interactive treemaps
  - [x] Dendrograms with clustering
  - [x] Sunburst charts
  - [x] Circular treemaps

- [x] **Interactive Dashboard**
  - [x] streamlit_app.py
  - [x] Multi-page navigation
  - [x] requirements.txt

- [x] **Analysis Notebook**
  - [x] 01_hierarchical_analysis.ipynb
  - [x] All sections completed
  - [x] Markdown annotations

- [x] **Processing Scripts**
  - [x] paises.py
  - [x] companys.py
  - [x] budget.py

- [x] **Repository Files**
  - [x] README.md
  - [x] requirements.txt

---
##DASHBOARD LINK

https://advanced-data-visualization-technical-storytelling.streamlit.app/

=
**Version:** 1.0.0  
**Checkpoint:** 2 of 3  
**Status:** ✅ Complete
