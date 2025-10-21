import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Corporate Visualization Suite",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# LOAD DATA
# -----------------------------
BASE_DIR = Path(__file__).resolve().parents[2]  # repo root
DATA_DIR = BASE_DIR / "data_files" / "checkpoint2"

empresas_tech_path = DATA_DIR / "empresas_tech.csv"
population_continent_path = DATA_DIR / "gdp_population_and_continent_un_195_countries.csv"
budget_data_path = DATA_DIR / "budget_data.csv"

df_population = pd.read_csv(population_continent_path)
df_tech = pd.read_csv(empresas_tech_path)
df_budget = pd.read_csv(budget_data_path)

# -----------------------------
# DATA PREPARATION
# -----------------------------
# Population
df_population = df_population.rename(columns={
    'País': 'country',
    'Continente': 'continent',
    'PIB 2023 (USD corrientes)': 'gdp',
    'Poblacion Total 2023': 'population'
})
total_population = df_population['population'].sum()
top_continent = df_population.groupby('continent')['population'].sum().idxmax()
china_india_pop = df_population[df_population['country'].isin(['China','India'])]['population'].sum()

# Employees
total_employees = df_tech['values'].sum()
dept_counts = df_tech.groupby('labels')['values'].sum()
engineering_share = dept_counts.get('Engineering',0)/total_employees*100
tech_departments = ['Engineering','IT']
technical_share = dept_counts[dept_counts.index.isin(tech_departments)].sum()/total_employees*100
non_technical_share = 100 - technical_share
top_dept = dept_counts.idxmax()

# Budget
total_budget = df_budget['budget'].sum()
dept_budget_share = df_budget.groupby('department')['budget'].sum()/total_budget*100
engineering_budget_share = dept_budget_share.get('Engineering',0)
largest_project = df_budget.loc[df_budget['budget'].idxmax(),'project']

# -----------------------------
# PAGE HEADER
# -----------------------------
st.title("💼 Corporate Data Dashboard")
st.markdown("""
Welcome to the **Corporate Visualization Suite**, an interactive analytics dashboard for technical audiences.  
Below is a summary of the datasets you'll explore:
""")
# -----------------------------
# KPIs BLOCKS
# -----------------------------
st.markdown("### 🌍 World Population")
col1, col2, col3 = st.columns(3)
col1.metric("Total Population", f"{total_population/1e6:.1f}M")
col2.metric("Largest Continent by Pop", top_continent)
col3.metric("China + India", f"{china_india_pop/1e6:.0f}M people")

# Small preview chart
fig_pop = px.bar(df_population.groupby('continent')['population'].sum().sort_values(ascending=False).reset_index(),
                 x='continent', y='population',
                 title="Population by Continent")
st.plotly_chart(fig_pop, use_container_width=True)

# -----------------------------
st.markdown("### 👥 Organizational Structure")
col1, col2, col3 = st.columns(3)
col1.metric("Total Employees", f"{total_employees}")
col2.metric("Engineering %", f"{engineering_share:.1f}%")
col3.metric("Technical vs Non-Tech", f"{technical_share:.1f}% / {non_technical_share:.1f}%")

# Pie preview
fig_emp = px.pie(names=dept_counts.index, values=dept_counts.values, title="Employees by Department")
fig_emp.update_traces(textinfo='label+percent', hole=0.4)
st.plotly_chart(fig_emp, use_container_width=True)

# -----------------------------
st.markdown("### 💰 Budget Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Total Budget", f"${total_budget:,.0f}K")
col2.metric("Engineering Budget %", f"{engineering_budget_share:.1f}%")
col3.metric("Largest Project", largest_project)

# Mini treemap
fig_budget = px.treemap(df_budget, path=['department','project'], values='budget', title="Budget Distribution")
st.plotly_chart(fig_budget, use_container_width=True)

# -----------------------------
st.markdown("---")
st.markdown("""
### 📌 Key Takeaways
- Asia dominates global population, with China + India alone representing a huge share.
- Engineering and IT departments represent the bulk of technical workforce.
- The budget dataset shows resource allocation across departments and highlights the largest projects.
- Explore the sidebar to see detailed interactive visualizations.
""")
