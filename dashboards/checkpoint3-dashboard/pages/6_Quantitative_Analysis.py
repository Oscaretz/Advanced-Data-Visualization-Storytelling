import streamlit as st
import pandas as pd

# -----------------------------
# LOAD DATA
# -----------------------------
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]  # repo root
DATA_DIR = BASE_DIR / "data_files" / "checkpoint2"

population_continent_path = DATA_DIR / "gdp_population_and_continent_un_195_countries.csv"
empresas_tech_path = DATA_DIR / "empresas_tech.csv"
budget_data_path = DATA_DIR / "budget_data.csv"

df_population = pd.read_csv(population_continent_path)
df_tech = pd.read_csv(empresas_tech_path)
df_budget = pd.read_csv(budget_data_path)

# -----------------------------
# DATA PREPARATION
# -----------------------------
df_population = df_population.rename(columns={
    'País': 'country',
    'Continente': 'continent',
    'PIB 2023 (USD corrientes)': 'gdp',
    'Poblacion Total 2023': 'population'
})

total_population = df_population['population'].sum()
continent_share = df_population.groupby('continent')['population'].sum() / total_population * 100
china_india_pop = df_population[df_population['country'].isin(['China', 'India'])]['population'].sum()
gdp_stats = df_population.groupby('continent')['gdp'].mean()

total_employees = df_tech['values'].sum()
dept_counts = df_tech.groupby('labels')['values'].sum()
engineering_share = dept_counts.get('Engineering', 0) / total_employees * 100
tech_departments = ['Engineering', 'IT']
technical_share = dept_counts[dept_counts.index.isin(tech_departments)].sum() / total_employees * 100
non_technical_share = 100 - technical_share

total_budget = df_budget['budget'].sum()
dept_budget_share = df_budget.groupby('department')['budget'].sum() / total_budget * 100
engineering_budget_share = dept_budget_share.get('Engineering', 0)
largest_project = df_budget.loc[df_budget['budget'].idxmax(), 'project']

# -----------------------------
# PAGE TITLE
# -----------------------------
st.title("📈 Final Quantitative Analysis & Insights")

# -----------------------------
# WORLD POPULATION
# -----------------------------
st.subheader("🌍 World Population")
st.metric("Total Population (million)", f"{total_population/1e6:.0f}")
st.dataframe(continent_share.rename("Population % by Continent"))

st.markdown(f"**China + India population:** {china_india_pop/1e6:.0f}M people")

st.markdown("**Average GDP per continent (USD)**")
st.dataframe(gdp_stats)

# -----------------------------
# ORGANIZATIONAL STRUCTURE
# -----------------------------
st.subheader("🏢 Organizational Structure")
st.metric("Total Employees", total_employees)
st.markdown(f"**Engineering:** {engineering_share:.1f}% of employees ({dept_counts.get('Engineering',0)}/{total_employees})")
st.markdown(f"**Technical vs Non-Technical:** {technical_share:.1f}% / {non_technical_share:.1f}%")

# -----------------------------
# BUDGET
# -----------------------------
st.subheader("💰 Budget Overview")
st.metric("Total Budget (K USD)", f"{total_budget:,.0f}")
st.markdown(f"**Engineering:** {engineering_budget_share:.1f}% of total budget")
st.markdown(f"**Largest Project:** {largest_project}")

st.markdown("### Budget % by Department")
st.dataframe(dept_budget_share.round(2))

# -----------------------------
# COMPARISON OF TECHNIQUES
# -----------------------------
st.subheader("⚖️ Comparison of Visualization Techniques")
st.markdown("""
| Technique   | Advantages                   | Disadvantages                 | Best For                          |
|------------|------------------------------|-------------------------------|----------------------------------|
| Treemap    | Efficient use of space       | Hard to see deep structure    | Medium to large datasets         |
| Dendrogram | Clear hierarchy              | Does not show magnitudes      | Clustering analysis              |
| Sunburst   | Multiple levels              | Labels can be hard to read    | Organizational structures        |
| Bar Chart  | Easy comparison              | Does not show hierarchy       | Small datasets                   |
""")

st.subheader("🔍 Analysis Insights")
st.markdown(f"""
**World Population:**  
- **Asia:** {continent_share.get('Asia', 0):.1f}% of the global population  
- **China + India:** ~{china_india_pop/1e6:.0f} million people  
- Significant disparities in GDP per capita across continents:  
""")
for cont, gdp in gdp_stats.items():
    st.markdown(f"  - **{cont}:** {gdp:.2e} USD")

st.markdown(f"""
**Organizational Structure:**  
- **Engineering:** {engineering_share:.1f}% of employees ({dept_counts.get('Engineering',0)}/{total_employees})  
- Technical vs Non-Technical balance: {technical_share:.1f}% / {non_technical_share:.1f}%  

**Budget:**  
- **Engineering:** {engineering_budget_share:.1f}% of total budget  
- **Largest project:** {largest_project}
""")
