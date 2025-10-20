import streamlit as st
from datetime import datetime
from pathlib import Path
import pandas as pd
import plotly.express as px
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import geopandas as gpd
import numpy as np  
import plotly.express as px
from statsmodels.tsa.stattools import ccf
import os
import seaborn as sns
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# from modules.time_series import plot_random_walk_analysis
# from modules.spatial_analysis import plot_geo_interest
# from modules.integration import plot_correlation_heatmap


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# # ======= GLOBAL BACKGROUND FIX =======
# page_bg = """
# <style>
# [data-testid="stAppViewContainer"] {
#     background-color: #ffffff;
# }
# [data-testid="stHeader"] {
#     background: none;
# }
# [data-testid="stToolbar"] {
#     right: 2rem;
# }
# </style>
# """
# st.markdown(page_bg, unsafe_allow_html=True)

#######################
# DUMMY TEST FUNCTION
#######################
def test_func():
    data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D'],
        'Value': [23, 45, 12, 67]
    })

    fig = px.bar(
        data,
        x='Category',
        y='Value',
        title='Dummy Test Chart',
        color='Category',
        color_discrete_sequence=['#0E3B43', '#1C6E8C', '#274156', '#C1A57B']
    )

    fig.update_layout(
        template='plotly_white',
        title_font=dict(size=22, family='Helvetica', color='#0E3B43'),
        font=dict(family='Helvetica', color='#1A1A1A'),
        xaxis_title='Category',
        yaxis_title='Value',
        plot_bgcolor='rgba(250,250,250,1)',
        paper_bgcolor='rgba(255,255,255,1)',
        margin=dict(l=40, r=40, t=80, b=40),
    )
    return fig


# ------------------------
#LOADING DATA 
# Base del script
BASE_DIR = Path(__file__).resolve().parent

# Carpeta de datos (sube dos niveles hasta el repo raíz y entra a data_files/checkpoint1)
DATA_DIR = BASE_DIR.parent.parent / "data_files" / "checkpoint1"

# Archivos de datos
trends_fp = DATA_DIR / "trends_enriched.csv"
geojson_fp = DATA_DIR / "geo_countries.geojson"
country_agg_fp = DATA_DIR / "country_aggregated.csv"
integrated_fp = DATA_DIR / "integrated_data.csv"

# Verificar existencia
for fp in [trends_fp, geojson_fp, country_agg_fp, integrated_fp]:
    if not fp.exists():
        print(f"⚠️ Archivo no encontrado: {fp}")


# --- Cargar y procesar datos (cacheado) ---
@st.cache_data
def load_trends_data(fp):
    df = pd.read_csv(fp, parse_dates=['date'])
    #df['date'] = pd.to_datetime(df['date']).dt.date
    return df

df_trends = load_trends_data(trends_fp)

# --- Función para preparar datos del mapa (cacheada) ---
@st.cache_data
def prepare_map_data(df):
    df_anim = df.copy()
    df_anim['month'] = pd.to_datetime(df_anim['date']).dt.to_period('M').astype(str)

    top_countries = df_anim.groupby('iso3')['interest'].mean().sort_values(ascending=False).head(10).index
    df_top = df_anim[df_anim['iso3'].isin(top_countries)]

    df_top['interest_percentile'] = df_top.groupby('month')['interest'].rank(pct=True) * 100
    return df_top

df_top = prepare_map_data(df_trends)

# --- Función para crear figura del mapa (cacheada) ---
@st.cache_resource
def create_map(df_top):
    vmin = df_top['interest'].quantile(0.10)
    vmax = df_top['interest'].quantile(0.90)

    fig_anim = px.choropleth(
        df_top,
        locations='iso3',
        color='interest_percentile',
        hover_name='name',
        hover_data={
            'interest_percentile': ':.1f',
            'iso3': False
        },
        animation_frame='month',
        range_color=[vmin, vmax],
        color_continuous_scale='RdYlBu_r',
        projection='natural earth',
        title='Monthly Evolution of Interest in Cryptocurrencies (Top 10 Countries)'
    )

    fig_anim.update_layout(
        coloraxis_colorbar=dict(title="Interest<br>Percentile", tickformat='.1f'),
        geo=dict(showframe=False, showcoastlines=True, coastlinecolor='lightgray'),
        height=600
    )

    # Ajustar velocidad de animación
    fig_anim.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 800
    fig_anim.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 300
    return fig_anim

# ------ 3.1

# =========================
# Cargar datos integrados con cache
# =========================
@st.cache_data
def load_integrated_data(fp):
    df = pd.read_csv(fp, parse_dates=['Date'])
    # Limpieza básica
    df = df.dropna(subset=["lat", "lon", "iso3", "interest"])
    df["Volume"] = df["Volume"].astype(float)
    return df

df_integrated = load_integrated_data(integrated_fp)

# =========================
# Función 1: Proportional Symbol Map Optimizada
# =========================
@st.cache_resource
def create_symbol_map_optimized(df, lat_col='lat', lon_col='lon', size_col='Volume',
                                color_col='region', hover_name='country',
                                top_n=50, title="Total Watch Time by Geographic Location"):
    """
    Crea un mapa proporcional optimizado para grandes volúmenes de datos.
    Args:
        df (pd.DataFrame): DataFrame con columnas lat, lon, size_col, color_col, hover_name
        top_n (int): Mostrar solo los top N por Volume
    Returns:
        fig (plotly.graph_objects.Figure)
    """
    if df.empty:
        return None

    # Resumir por país para reducir puntos
    df_summary = df.groupby(hover_name, as_index=False).agg({
        lat_col: 'first',
        lon_col: 'first',
        size_col: 'sum',
        color_col: 'first'
    })

    # Seleccionar top N por volumen
    df_top = df_summary.nlargest(top_n, size_col).copy()

    # Log-transform para que los puntos no exploten visualmente
    df_top['size_log'] = np.log1p(df_top[size_col])

    fig = px.scatter_geo(
        df_top,
        lat=lat_col,
        lon=lon_col,
        size='size_log',
        color=color_col,
        hover_name=hover_name,
        projection="natural earth",
        title=title
    )

    fig.update_traces(
        marker=dict(opacity=0.7, sizemode='area', 
                    sizeref=2.*df_top['size_log'].max()/(100.**2), sizemin=4)
    )

    fig.update_layout(
        geo=dict(showland=True, landcolor="LightGreen"),
        margin=dict(l=20, r=20, t=50, b=20),
        template='plotly_white'
    )

    return fig


# =========================
# Función 2: Flow Map Optimizada
# =========================
@st.cache_resource
def create_flow_map_optimized(df, top_n=5, interest_col='interest',
                              lat_col='lat', lon_col='lon', country_col='country',
                              title="Content Popularity Spread Across Regions"):
    """
    Crea un Flow Map optimizado mostrando solo los top N flujos de interés.
    Args:
        df (pd.DataFrame)
        top_n (int): Cantidad de países a mostrar en flujo
    Returns:
        flow_fig (plotly.graph_objects.Figure)
    """
    if df.empty:
        return None

    # Seleccionar top N por interés
    top_countries = df.nlargest(top_n, interest_col)[[country_col, lat_col, lon_col]].values

    flow_fig = go.Figure()

    # Conectar solo países consecutivos del top
    for i in range(len(top_countries) - 1):
        flow_fig.add_trace(go.Scattergeo(
            lon=[top_countries[i][2], top_countries[i+1][2]],
            lat=[top_countries[i][1], top_countries[i+1][1]],
            mode="lines+markers",
            line=dict(width=2, color="blue"),
            marker=dict(size=6, color="red"),
            hoverinfo='text',
            hovertext=[f"{top_countries[i][0]} → {top_countries[i+1][0]}"]
        ))

    flow_fig.update_layout(
        title=title,
        geo=dict(projection_type='natural earth', showland=True, landcolor="LightGreen"),
        margin=dict(l=20, r=20, t=50, b=20),
        template='plotly_white'
    )

    return flow_fig



# xxxxxxxxxxxxxxxxxxxxxx

# # --- Función para preparar datos de la serie temporal mensual ---
# @st.cache_data
# def prepare_ts_data(region_ts, df_trends):
#     df = region_ts.copy()
#     df['year_month'] = df['date'].dt.to_period('M').dt.to_timestamp()
#     return df

# # --- Función para obtener top N criptos globalmente ---
# @st.cache_data
# def get_top_cryptos(df_trends, top_n=4):
#     return df_trends.groupby('keyword')['interest'].mean().sort_values(ascending=False).index.tolist()[:top_n]

# # --- Función para crear gráfico interactivo con Plotly ---
# def plot_region_ts_interactive(df, selected_regions, selected_cryptos):
#     df_plot = df[df['region'].isin(selected_regions) & df['keyword'].isin(selected_cryptos)]
    
#     if df_plot.empty:
#         st.warning("No hay datos para la selección actual.")
#         return None
    
#     fig = px.line(
#         df_plot,
#         x='year_month',
#         y='interest_rolling3',
#         color='keyword',
#         facet_row='region',
#         facet_row_spacing=0.05,
#         labels={
#             'year_month': 'Fecha (mes)',
#             'interest_rolling3': 'Interest (rolling 3 wk mean)',
#             'keyword': 'Crypto'
#         },
#         hover_data={'keyword': True, 'region': True, 'year_month': True, 'interest_rolling3': ':.2f'}
#     )
    
#     fig.update_layout(
#         height=300 * len(selected_regions),
#         legend_title_text='Crypto',
#         margin=dict(l=40, r=40, t=60, b=40)
#     )
    
#     for axis in fig.layout:
#         if axis.startswith('xaxis'):
#             fig.layout[axis].tickangle = 30
    
#     return fig

# xxxxxxxxxxxxxxxxxxxxxx

@st.cache_data
def prepare_region_ts(df_trends):
    df_ts = df_trends.copy()
    
    # Asegurarse de que 'date' sea datetime
    df_ts['date'] = pd.to_datetime(df_ts['date'])
    
    # Agrupar por region, date y crypto (media interest)
    region_ts = df_ts.groupby(['region', 'date', 'keyword'], as_index=False)['interest'].mean()
    
    # Suavizar con media móvil de 3 periodos
    region_ts['interest_rolling3'] = region_ts.groupby(['region', 'keyword'])['interest'].transform(
        lambda x: x.rolling(3, min_periods=1).mean()
    )
    
    # Crear columna year_month para reducir puntos
    region_ts['year_month'] = region_ts['date'].dt.to_period('M').dt.to_timestamp()
    
    return region_ts
region_ts = prepare_region_ts(df_trends)
top_cryptos = df_trends.groupby('keyword')['interest'].mean().sort_values(ascending=False).index.tolist()[:5]

@st.cache_resource
def plot_region_ts_interactive(df, selected_regions, selected_cryptos):
    df_plot = df[df['region'].isin(selected_regions) & df['keyword'].isin(selected_cryptos)].copy()
    
    if df_plot.empty:
        st.warning("No hay datos para la selección actual.")
        return None

    # Crear columna para mostrar el nombre del continente bonito
    df_plot['region_label'] = df_plot['region'].map(lambda x: x.title())

    # Ordenar categorías para mantener consistencia
    region_order = df_plot['region_label'].unique()
    
    fig = px.line(
        df_plot,
        x='year_month',
        y='interest_rolling3',
        color='keyword',
        facet_row='region_label',
        facet_row_spacing=0.05,
        category_orders={"region_label": region_order},
        labels={
            'year_month': 'Fecha (mes)',
            'interest_rolling3': 'Interest (rolling 3 wk mean)',
            'keyword': 'Crypto',
            'region_label': 'Continent'
        },
        hover_data={'keyword': True, 'region': True, 'year_month': True, 'interest_rolling3': ':.2f'},
    )

    fig.update_layout(
        height=300 * len(selected_regions),
        legend_title_text='Crypto',
        margin=dict(l=80, r=40, t=60, b=40),
        template='plotly_white'
    )

    # Rotar ticks del eje x
    for axis in fig.layout:
        if axis.startswith('xaxis'):
            fig.layout[axis].tickangle = 30

    return fig

@st.cache_resource
def plot_top_countries_interactive(df, top_n=10):
    """
    Crea un gráfico de barras interactivo con los top N países por interés medio.

    Args:
        df (pd.DataFrame): DataFrame con al menos las columnas ['name', 'interest_mean'].
        top_n (int): Número de países a mostrar.
    Returns:
        fig (plotly.graph_objects.Figure): Figura interactiva.
    """
    # Seleccionar top N países
    top_df = df.nlargest(top_n, 'interest_mean')

    # Crear figura interactiva
    fig = px.bar(
        top_df,
        x='interest_mean',
        y='name',
        orientation='h',
        color='interest_mean',
        color_continuous_scale='viridis',
        text='interest_mean',
        labels={'interest_mean': 'Interest (media)', 'name': 'Country'},
        hover_data={'name': True, 'interest_mean': ':.2f'}
    )

    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    
    fig.update_layout(
        #title=f'Top {top_n} países por interés medio (Oct 2020 - Oct 2025)',
        yaxis=dict(autorange="reversed"),  # Para que el top 1 quede arriba
        template='plotly_white',
        margin=dict(l=100, r=40, t=60, b=40),
        height=400 + top_n*20,
        coloraxis_showscale=False
    )

    return fig

# ----- part 3.2 ----------

# =========================
# Cargar datos optimizado con cache
# =========================
@st.cache_data
def load_integrated_data2(fp):
    df = pd.read_csv(fp, parse_dates=['Date'])
    df = df.rename(columns={'Date': 'date'})
    df = df.dropna(subset=['crypto', 'country_code', 'interest', 'volatility_7d'])
    return df


# =========================
# calcular CCF optimizado
# =========================
@st.cache_data
def compute_ccf(df, crypto, countries, max_lag=8):
    """
    Calcula el Cross-Correlation Function (CCF) entre interés y volatilidad para cada país.
    """
    results = {}

    for country in countries:
        subset = df[(df['crypto'] == crypto) & (df['country_code'] == country)].copy()
        subset = subset.sort_values('date')

        if subset[['interest', 'volatility_7d']].dropna().empty:
            continue

        # Z-score normalization
        subset['interest_z'] = (subset['interest'] - subset['interest'].mean()) / subset['interest'].std()
        subset['volatility_z'] = (subset['volatility_7d'] - subset['volatility_7d'].mean()) / subset['volatility_7d'].std()

        # Compute CCF
        ccf_full = np.correlate(
            subset['interest_z'] - subset['interest_z'].mean(),
            subset['volatility_z'] - subset['volatility_z'].mean(),
            mode='full'
        )
        ccf_full = ccf_full / (np.std(subset['interest_z']) * np.std(subset['volatility_z']) * len(subset))

        center_idx = len(ccf_full)//2
        lags = np.arange(-max_lag, max_lag+1)
        ccf_plot = ccf_full[center_idx-max_lag:center_idx+max_lag+1]

        results[country] = (lags, ccf_plot)
    return results


# =========================
# Graficar dinámico con Matplotlib
# =========================
def plot_ccf_results(results, crypto):
    """
    Plotea los resultados de CCF por país.
    """
    if not results:
        st.warning("No hay datos suficientes para mostrar el gráfico.")
        return

    countries = list(results.keys())
    fig, axes = plt.subplots(len(countries), 1, figsize=(8, 3*len(countries)), sharex=True)
    fig.suptitle(f'Lead-Lag Analysis (CCF): Google Trends vs Volatility ({crypto})', fontsize=14)

    # Si solo hay 1 país, axes no es lista
    if len(countries) == 1:
        axes = [axes]

    for ax, country in zip(axes, countries):
        lags, ccf_plot = results[country]
        ax.bar(lags, ccf_plot, width=0.6, color='skyblue', edgecolor='black')
        ax.axhline(0, color='gray', linestyle='--', linewidth=1)
        ax.axvline(0, color='red', linestyle='--', linewidth=1)
        ax.set_title(f"{country} — Peak correlation lag: {lags[np.argmax(ccf_plot)]}")
        ax.set_ylabel("CCF")

    axes[-1].set_xlabel("Lag (weeks)")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    st.pyplot(fig)


# =========================
# 4Bloque de ejecución Streamlit
# =========================
def section2_ccf_analysis(integrated_fp):
    st.header("📈 Sección 2 — Análisis Lead-Lag (Google Trends vs Volatilidad)")

    # Cargar datos
    df_int = load_integrated_data2(integrated_fp)

    # Selecciones dinámicas
    cryptos = sorted(df_int['crypto'].unique())
    countries_all = sorted(df_int['country_code'].unique())

    crypto = st.selectbox("Selecciona la criptomoneda:", cryptos, index=cryptos.index('Bitcoin') if 'Bitcoin' in cryptos else 0)
    selected_countries = st.multiselect("Selecciona países para comparar:", countries_all, default=['US', 'IN', 'JP', 'BR', 'DE'])
    max_lag = st.slider("Selecciona el máximo lag (semanas):", 1, 12, 8)

    if st.button("Calcular CCF"):
        with st.spinner("Calculando correlaciones cruzadas..."):
            results = compute_ccf(df_int, crypto, selected_countries, max_lag)
            plot_ccf_results(results, crypto)

# ------part 3.2 ----

# ===============================
# 1Clustered Map — Country Distribution
# ===============================
@st.cache_data(show_spinner=False)
def get_clustered_map(df):
    """Genera un mapa con clustering de marcadores para representar países."""
    try:
        # Promedio global de coordenadas
        avg_lat, avg_lon = df["lat"].mean(), df["lon"].mean()
        m = folium.Map(location=[avg_lat, avg_lon], zoom_start=2, tiles="CartoDB positron")
        cluster = MarkerCluster().add_to(m)

        for _, row in df.iterrows():
            popup_text = f"<b>{row['country']}</b><br>Volumen: {row['Volume']:.2f}<br>Interés: {row['interest']}"
            folium.Marker(
                location=[row["lat"], row["lon"]],
                popup=popup_text,
                tooltip=row["country"],
                icon=folium.Icon(color="blue", icon="info-sign")
            ).add_to(cluster)

        return m
    except Exception as e:
        st.error(f"⚠️ Error al generar el mapa clusterizado: {e}")
        return None


# ===============================
# 2️Cartogram — Revenue Proxy (Volume)
# ===============================
@st.cache_data(show_spinner=False)
@st.cache_data(show_spinner=False)
def get_cartogram(df):
    """Genera un cartograma de volumen (revenue proxy) con shapefile externo."""
    try:
        shapefile_url = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"
        shapefile_path = "data_files/world_shape.zip"

        # Descargar shapefile si no existe
        if not os.path.exists(shapefile_path):
            import requests
            os.makedirs("data_files", exist_ok=True)
            r = requests.get(shapefile_url)
            with open(shapefile_path, "wb") as f:
                f.write(r.content)

        # Cargar el shapefile y mergear con df
        world = gpd.read_file(f"zip://{os.path.abspath(shapefile_path)}")
        merged = world.merge(df, left_on="ISO_A3", right_on="iso3", how="left")

        fig, ax = plt.subplots(figsize=(10, 5))
        merged.plot(
            column="Volume",
            cmap="OrRd",
            linewidth=0.5,
            edgecolor="0.8",
            legend=True,
            ax=ax,
        )
        ax.set_title("Countries Sized by Revenue Contribution", fontsize=13)
        ax.axis("off")
        plt.tight_layout()
        return fig

    except Exception as e:
        st.warning(f"⚠️ No se pudo generar el cartograma: {e}")
        return None


# =========================
# PAGE CONFIGURATION
# =========================
st.set_page_config(
    page_title="Cryptocurrency Spatiotemporal Analysis",
    layout="wide"
)


# =========================
# LOAD CUSTOM STYLES
# =========================
# Función para cargar CSS personalizado
def load_css(file_path: Path):
    """Carga un archivo CSS externo en Streamlit."""
    try:
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"⚠️ No se encontró el archivo CSS: {file_path}")

# Ruta al archivo CSS (ajustado a la estructura del repo)
CSS_PATH = Path(__file__).parent.parent / "assets" / "style.css"

# Cargar estilos
load_css(CSS_PATH)


# =========================
# HEADER
# =========================
st.markdown("""
<div class="main-header">
    <h1>Cryptocurrency Spatiotemporal Analysis Dashboard</h1>
    <p class="subheader">An executive overview of temporal patterns, geographic adoption, and predictive insights.</p>
</div>
""", unsafe_allow_html=True)

st.divider()


# =========================
# KPI SECTION
# =========================
st.markdown("### Key Market Indicators [WIP]") 

col1, col2, col3 = st.columns(3)

with col1:
    with st.container():
        st.metric("Top Performing Coin", "Bitcoin (BTC)", "+3.2% (24h)")

with col2:
    with st.container():
        st.metric("Global Adoption Index", "82.4%", "↑ 1.8% MoM")

with col3:
    with st.container():
        st.metric("Average Volatility", "5.6%", "↓ 0.7% WoW")

st.divider()


# =========================
# MAIN TABS
# =========================
tab1, tab2, tab3 = st.tabs([
    "Time Series Analysis",
    "Spatial Analysis",
    "Spatiotemporal Integration"
])

# ----- Time Series Tab -----
with tab1:
    st.subheader("Time Series Analysis")

    col1, col2 = st.columns([1, 2])
    with col1:
        crypto = st.selectbox("Choose a crypto:", ["BNB", "BTC", "SOLANA", "TETHER", "ETH"], key="crypto1")
    with col2:
        analysis = st.radio(
            "Choose an analysis:",
            ["Random Walk Test", "Autocorrelation", "Volatility"],
            horizontal=True,
            key="subtab1"
        )

    st.markdown("---")

    GRAPH_DIR = BASE_DIR.parent / "assets" / "graphs"

    if analysis == "Random Walk Test":
        st.image(GRAPH_DIR / f"BNB_RWvsS_{crypto}.png", caption=f"Random Walk vs Serie ({crypto})")
        st.write("Interpretation of random walk test...")
    elif analysis == "Autocorrelation":
        st.image(GRAPH_DIR / f"ACF_{crypto}.png", caption=f"Autocorrelation of Returns ({crypto})")
    elif analysis == "Volatility":
        st.image(GRAPH_DIR / f"VOL_{crypto}.png")
        st.image(GRAPH_DIR / f"VOLU_{crypto}.png")
        st.image(GRAPH_DIR / f"VOLCOR_{crypto}.png")



    # test1 = test_func()
    # st.plotly_chart(test1, use_container_width=True, key='time_series')

# ----- Spatial Tab -----
with tab2:
    st.markdown("#### Spatial Analysis")
    st.write("""
    Explore global adoption patterns and visualize interest in cryptocurrencies across countries using Google Trends 
    and exchange distribution data.
    """)
    # Solo crear el mapa cuando se entra a la pestaña
    fig_map = create_map(df_top)
    st.plotly_chart(fig_map, use_container_width=True)

    # -------------
    st.markdown("#### Time Series by Region")

    # Preparar datos de series temporales
    region_ts_processed = prepare_region_ts(df_trends)

    # Widgets multiselección
    regions = region_ts_processed['region'].dropna().unique().tolist()
    selected_regions = st.multiselect("Select Regions", regions, default=regions[:3])

    selected_cryptos = st.multiselect("Select Cryptos", top_cryptos, default=top_cryptos[:4])

    # Crear y mostrar figura
    fig = plot_region_ts_interactive(region_ts_processed, selected_regions, selected_cryptos)
    st.plotly_chart(fig, use_container_width=True)
    # ----
    st.markdown("#### Top 10 countries by average interest:")
    country_mean = df_trends.groupby(['iso3','name','country','region'], as_index=False)['interest'].agg(
        interest_mean='mean', interest_std='std', interest_max='max'
        )
    country_mean = country_mean.sort_values('interest_mean', ascending=False)
    fig_top_countries = plot_top_countries_interactive(country_mean, top_n=10)
    st.plotly_chart(fig_top_countries, use_container_width=True)


    


# ----- Integration Tab -----
with tab3:
    st.markdown("#### Spatiotemporal Integration")

   # =========================
    # SECCIÓN 1: Mapas
    # =========================
    with st.container():
        st.markdown("##### Section 1: Maps Overview")

        # --- Sub-bloque 1: dos mapas lado a lado ---
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                df_integrated = load_integrated_data(integrated_fp)
                symbol_map_fig = create_symbol_map_optimized(df_integrated, top_n=50)
                st.plotly_chart(symbol_map_fig, use_container_width=True)

                
            with col2:
                flow_map_fig = create_flow_map_optimized(df_integrated, top_n=10)
                st.plotly_chart(flow_map_fig, use_container_width=True)

        # --- Sub-bloque 2: mapa debajo de los dos anteriores ---
        with st.container():
            with st.container(border=True):
                st.subheader("Clustered Map — Global Distribution")
                clustered_map = get_clustered_map(df_integrated)
                if clustered_map:
                    st_folium(clustered_map, width=800, height=500, key="cluster_map")

            with st.container(border=True):
                st.subheader("Cartogram — Revenue Proxy (Volume)")
                cartogram_fig = get_cartogram(df_integrated)
                if cartogram_fig:
                    st.pyplot(cartogram_fig, use_container_width=True, clear_figure=True)

                #st.divider()  # Separación visual entre secciones

    # =========================
    # SECCIÓN 2: Gráfica
    # =========================
    with st.container():
        st.markdown("##### Section 2: Correlation / Insights")

        section2_ccf_analysis(integrated_fp)






# =========================
# FOOTER
# =========================
st.markdown(f"""
<div class="footer">
    <p>Developed for <b>Spatiotemporal Analysis Case Studies - Data Engineering Program</b></p>
    <p>© {datetime.now().year} Crypto Analytics Dashboard</p>
</div>
""", unsafe_allow_html=True)
