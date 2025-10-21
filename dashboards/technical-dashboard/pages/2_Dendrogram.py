import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from scipy.spatial.distance import pdist
from sklearn.preprocessing import StandardScaler
import plotly.figure_factory as ff

# -----------------------------
# LOAD DATA
# -----------------------------
BASE_DIR = Path(__file__).resolve().parents[3]  # repo root
DATA_DIR = BASE_DIR / "data_files" / "checkpoint2"

population_continent_path = DATA_DIR / "gdp_population_and_continent_un_195_countries.csv"
df = pd.read_csv(population_continent_path)

st.title("🌳 Hierarchical Clustering Dendrogram")

# -----------------------------
# Prepare data
# -----------------------------
df = df.dropna(subset=['PIB 2023 (USD corrientes)', 'Poblacion Total 2023']).copy()
df['PIB per capita'] = df['PIB 2023 (USD corrientes)'] / df['Poblacion Total 2023']

features = df[['Poblacion Total 2023', 'PIB per capita']].values
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# -----------------------------
# Distance matrix & linkage
# -----------------------------
distances = pdist(features_scaled, metric='euclidean')
linkage_matrix = linkage(distances, method='ward')

# -----------------------------
# Streamlit interactive threshold
# -----------------------------
threshold = st.slider("Cluster distance threshold", min_value=1.0, max_value=20.0, value=5.0, step=0.5)

# -----------------------------
# Plot dendrogram with Plotly
# -----------------------------
fig = ff.create_dendrogram(
    features_scaled,
    labels=df['País'].values,
    linkagefun=lambda x: linkage(x, method='ward'),
    color_threshold=threshold
)
fig.update_layout(
    width=1200,
    height=600,
    title="Hierarchical Clustering Dendrogram | Countries grouped by Population & GDP per Capita",
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Clusters interpretation
# -----------------------------
clusters = fcluster(linkage_matrix, t=threshold, criterion='distance')
df['Cluster'] = clusters
n_clusters = len(np.unique(clusters))

st.markdown(f"**Number of clusters formed:** {n_clusters}")

for i in range(1, n_clusters + 1):
    countries = df.loc[df['Cluster'] == i, 'País'].values
    st.write(f"**Cluster {i}:** {', '.join(countries[:10])}{'...' if len(countries) > 10 else ''}")
