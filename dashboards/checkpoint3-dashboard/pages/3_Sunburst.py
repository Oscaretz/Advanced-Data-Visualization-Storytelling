import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.graph_objects as go

# -----------------------------
# LOAD DATA
# -----------------------------
BASE_DIR = Path(__file__).resolve().parents[3]  # repo root
DATA_DIR = BASE_DIR / "data_files" / "checkpoint2"

empresas_tech_path = DATA_DIR / "empresas_tech.csv"
df = pd.read_csv(empresas_tech_path)

st.title("☀️ Sunburst Chart - Organizational Structure")

# -----------------------------
# Sunburst Chart
# -----------------------------
fig = go.Figure(go.Sunburst(
    labels=df['labels'],
    parents=df['parents'],
    values=df['values'],
    branchvalues="total",  # parent values include children
    marker=dict(
        colors=df['values'],
        colorscale='Viridis',
        cmid=df['values'].mean(),
        line=dict(color='white', width=2)
    ),
    hovertemplate='<b>%{label}</b><br>Value: %{value}<br>Percentage: %{percentParent:.1%}<extra></extra>',
    textfont=dict(size=11)
))

fig.update_layout(
    title='Organizational Structure - Tech Company<br>Sunburst Chart',
    width=900,
    height=900,
    font=dict(size=12)
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("💡 Tip: Click on any segment to zoom in.")
