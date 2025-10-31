# ==============================
# 1_Treemaps.py
# ==============================
import streamlit as st
from pathlib import Path
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import squarify  # for static treemap

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="Treemaps",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Treemaps - Corporate Data Visualization Suite")

# -----------------------------
# ROOT REPO
# -----------------------------
BASE_DIR = Path(__file__).resolve().parents[3]  # 3 niveles: streamlit_app.py -> technical-dashboard -> dashboards -> repo raíz

DATA_DIR = BASE_DIR / "data_files" / "checkpoint2"

budget_data_path = DATA_DIR / "budget_data.csv"
empresas_tech_path = DATA_DIR / "empresas_tech.csv"
population_continent_path = DATA_DIR / "gdp_population_and_continent_un_195_countries.csv"

# Verificar archivos
missing_files = [p for p in [budget_data_path, empresas_tech_path, population_continent_path] if not p.exists()]
if missing_files:
    st.error(f"❌ Could not find these datasets:\n{missing_files}")
    st.stop()

# Cargar CSVs
budget_data_df = pd.read_csv(budget_data_path)
empresas_tech_df = pd.read_csv(empresas_tech_path)
population_continent_df = pd.read_csv(population_continent_path)

st.success("✅ CSV files loaded successfully!")

# ==============================
# STATIC TREEMAP (matplotlib + squarify)
# ==============================
st.subheader("Static Treemap of World Population")
df_pop = population_continent_df.dropna(subset=['Poblacion Total 2023'])
sizes = df_pop['Poblacion Total 2023'].values
labels = [f"{country}\n{pop/1e6:.1f}M" for country, pop in zip(df_pop['País'], df_pop['Poblacion Total 2023'])]

# Colors por continente
continents = df_pop['Continente'].unique()
continent_colors = plt.cm.Set3(np.linspace(0, 1, len(continents)))
color_map = dict(zip(continents, continent_colors))
colors = [color_map[cont] for cont in df_pop['Continente']]

fig, ax = plt.subplots(figsize=(18, 10))
squarify.plot(
    sizes=sizes,
    label=labels,
    color=colors,
    alpha=0.8,
    text_kwargs={'fontsize': 9, 'weight': 'bold'},
    ax=ax
)
plt.axis('off')
plt.title('Treemap of World Population by Continent and Country (2023)', fontsize=18, weight='bold', pad=20)
legend_elements = [plt.Rectangle((0, 0), 1, 1, fc=color_map[cont], alpha=0.8, label=cont) for cont in continents]
plt.legend(handles=legend_elements, loc='upper left', fontsize=11)
st.pyplot(fig)

# ==============================
# INTERACTIVE TREEMAP (Plotly)
# ==============================
st.subheader("Interactive Treemap with GDP per Capita")

df_plotly = df_pop.copy()
df_plotly['PIB per capita'] = df_plotly['PIB 2023 (USD corrientes)'] / df_plotly['Poblacion Total 2023']

min_pib = df_plotly['PIB per capita'].min()
max_pib_rounded = df_plotly['PIB per capita'].max()

fig_interactive = px.treemap(
    df_plotly,
    path=['Continente', 'País'],
    values='Poblacion Total 2023',
    color='PIB per capita',
    hover_data=['Poblacion Total 2023', 'PIB 2023 (USD corrientes)', 'PIB per capita'],
    color_continuous_scale='RdYlGn',
    range_color=[min_pib, max_pib_rounded],
    title='Interactive World Population Treemap (2023)<br>Size = Population, Color = GDP per Capita'
)
fig_interactive.update_traces(textinfo="label+value", textfont_size=11)
fig_interactive.update_layout(height=700, width=1000)
st.plotly_chart(fig_interactive, use_container_width=True)
