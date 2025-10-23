import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

# -----------------------------
# LOAD DATA
# -----------------------------
BASE_DIR = Path(__file__).resolve().parents[3]  # repo root
DATA_DIR = BASE_DIR / "data_files" / "checkpoint2"

df_population = pd.read_csv(DATA_DIR / "gdp_population_and_continent_un_195_countries.csv")
df_tech = pd.read_csv(DATA_DIR / "empresas_tech.csv")
df_budget = pd.read_csv(DATA_DIR / "budget_data.csv")

# -----------------------------
# PAGE TITLE
# -----------------------------
st.title("⚖️ Comparison of visualization techniques")

# -----------------------------
# DATA PREPARATION
# -----------------------------
df_population = df_population.rename(columns={
    'País': 'country',
    'Continente': 'continent',
    'PIB 2023 (USD corrientes)': 'gdp',
    'Poblacion Total 2023': 'population'
})

# Population metrics
total_population = df_population['population'].sum()
continent_share = df_population.groupby('continent')['population'].sum() / total_population * 100

# Plot: population by continent
fig_pop = px.pie(
    continent_share.reset_index().rename(columns={'population':'share'}),
    names='continent',
    values='share',
    title='Population Share by Continent (%)'
)
st.plotly_chart(fig_pop, use_container_width=True)

# Organizational structure
total_employees = df_tech['values'].sum()
dept_counts = df_tech.groupby('labels')['values'].sum()
engineering_share = dept_counts.get('Engineering', 0) / total_employees * 100

fig_dept = px.bar(
    dept_counts.reset_index().rename(columns={'labels':'department', 'values':'employees'}),
    x='department',
    y='employees',
    title='Employees per Department'
)
st.plotly_chart(fig_dept, use_container_width=True)

# Budget
total_budget = df_budget['budget'].sum()
dept_budget_share = df_budget.groupby('department')['budget'].sum() / total_budget * 100

fig_budget = px.treemap(
    df_budget,
    path=['department', 'project'],
    values='budget',
    title='Budget Distribution by Department and Project'
)
st.plotly_chart(fig_budget, use_container_width=True)

# Metrics display
st.metric("Total Population", f"{total_population/1e6:.0f} M")
st.metric("Engineering % Employees", f"{engineering_share:.1f}%")
st.metric("Total Budget", f"${total_budget:,.0f} K")
