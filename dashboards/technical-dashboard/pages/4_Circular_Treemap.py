import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px

# -----------------------------
# LOAD DATA
# -----------------------------
BASE_DIR = Path(__file__).resolve().parents[3]  # repo root
DATA_DIR = BASE_DIR / "data_files" / "checkpoint2"

budget_data_path = DATA_DIR / "budget_data.csv"
budget_data = pd.read_csv(budget_data_path)

# -----------------------------
# PAGE TITLE
# -----------------------------
st.title("🌀 Circular Treemap - Company Budget Distribution")

# -----------------------------
# Basic Stats
# -----------------------------
budget_data["category"] = "Company Budget"

st.markdown(f"**Total budget:** ${budget_data['budget'].sum():,.0f}K")
st.markdown(f"**Departments:** {budget_data['department'].nunique()}")
st.markdown(f"**Projects:** {len(budget_data)}")

st.markdown("### Budget per Department")
dept_budget = budget_data.groupby("department")["budget"].agg(["sum", "count", "mean"]).round(0)
dept_budget.columns = ['Total ($K)', 'Projects', 'Avg per Project ($K)']
st.dataframe(dept_budget)

# -----------------------------
# Circular Treemap
# -----------------------------
fig = px.treemap(
    budget_data,
    path=['category', 'department', 'project'],
    values='budget',
    color='budget',
    color_continuous_scale='Viridis',
    title='Company Budget Distribution<br>by Department and Project (in $K)'
)

fig.update_traces(textinfo="label+value+percent parent", textfont_size=10)
fig.update_layout(height=700, width=1000)

st.plotly_chart(fig, use_container_width=True)

st.markdown("💡 Tip: Hover over segments to see budget per project and department.")
