import streamlit as st
from pathlib import Path
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Movie Dashboard Checkpoint 3",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# LOAD DATA
# -----------------------------


BASE_DIR = Path(__file__).resolve().parents[2]  # repo root
DATA_DIR = BASE_DIR / "data_files" / "checkpoint3"

popular_movies_path = DATA_DIR / "popular_movies.csv"
top_rated_movies_path = DATA_DIR / "top_rated_movies.csv"

df_popular = pd.read_csv(popular_movies_path)
df_top_rated = pd.read_csv(top_rated_movies_path)


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
CSS_PATH = Path(__file__).parent.parent / "assets" / "style3.css"

# Cargar estilos
load_css(CSS_PATH)

# -----------------------------
# DATA PREPARATION
# -----------------------------
# Palette
COLOR_KPI = "#1f77b4"

def prepare_movie_kpis(df):
    total_movies = len(df)
    avg_popularity = df['popularity'].mean()
    avg_vote = df['vote_average'].mean()
    most_popular = df.loc[df['popularity'].idxmax(),'title']
    highest_rated = df.loc[df['vote_average'].idxmax(),'title']
    total_votes = df['vote_count'].sum()
    top_language = df['original_language'].mode()[0]
    adult_count = df['adult'].sum()
    return {
        'total_movies': total_movies,
        'avg_popularity': avg_popularity,
        'avg_vote': avg_vote,
        'most_popular': most_popular,
        'highest_rated': highest_rated,
        'total_votes': total_votes,
        'top_language': top_language,
        'adult_count': adult_count
    }

kpis_popular = prepare_movie_kpis(df_popular)
kpis_top_rated = prepare_movie_kpis(df_top_rated)

def kpi_with_icon(icon_path, label, value, width=60):
    """Renderiza un KPI con ícono local sin romper compatibilidad en Streamlit."""
    col_icon, col_text = st.columns([1, 3])
    with col_icon:
        st.image(str(icon_path), width=width)
    with col_text:
        st.markdown(
            f"""
            <div style='display: flex; flex-direction: column; justify-content: center;'>
                <span style='font-size: 0.9rem; color: #555;'>{label}</span>
                <span style='font-size: 1.5rem; font-weight: 700; color: #222;'>{value}</span>
            </div>
            """,
            unsafe_allow_html=True
        )


# -----------------------------
# PAGE HEADER
# -----------------------------
st.title("Movies Dashboard - Checkpoint 3")
st.markdown("""
Welcome to the **Checkpoint 3 Movie Dashboard**, an interactive analytics suite to explore trends in popular and top-rated movies.  
The KPIs below summarize the key metrics of the datasets.
""")
st.markdown("---")


# -----------------------------
# KPIs: Popular Movies
# -----------------------------
st.markdown("### Popular Movies Overview")

icon_dir = Path(__file__).parent.parent / "assets" / "icons"

col1, col2, col3 = st.columns(3)
with col1:
    kpi_with_icon(icon_dir / "movies.png", "Total Movies", kpis_popular['total_movies'])
with col2:
    kpi_with_icon(icon_dir / "polarity.png", "Average Popularity", f"{kpis_popular['avg_popularity']:.1f}")
with col3:
    kpi_with_icon(icon_dir / "vote.png", "Average Vote", f"{kpis_popular['avg_vote']:.1f}")

col1, col2, col3 = st.columns([2, 2, 1])
col1.metric("Most Popular Movie", kpis_popular['most_popular'])
col2.metric("Highest Rated Movie", kpis_popular['highest_rated'])
col3.metric("Movies for Adults", kpis_popular['adult_count'])

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# Popular Movies Charts
# -----------------------------

cols = st.columns([1, 0.3, 1, 0.3, 1])
with cols[0]:


    fig_popularity = px.histogram(df_popular, x='popularity', nbins=20, title="Popularity Distribution",
                                color_discrete_sequence=[COLOR_KPI])
    # Centrar el título
    fig_popularity.update_layout(
        title={
            'text': "Popularity Distribution",
            'x': 0.5,           # centro horizontal
            'xanchor': 'center',
            'yanchor': 'top'
        },
        width=600,       # ancho de la figura
        height=350,      # alto de la figura
        bargap=0.2,      # espacio entre barras
        title_x=0.5      # centrar título
    )
    st.plotly_chart(fig_popularity, use_container_width=False)

with cols[2]:

    fig_vote = px.histogram(df_popular, x='vote_average', nbins=20, title="Vote Average Distribution",
                            color_discrete_sequence=[COLOR_KPI])
    # Centrar el título
    fig_vote.update_layout(
        title={
            'text': "Popularity Distribution",
            'x': 0.5,           # centro horizontal
            'xanchor': 'center',
            'yanchor': 'top'
        },
        width=600,       # ancho de la figura
        height=350,      # alto de la figura
        bargap=0.2,      # espacio entre barras
        title_x=0.5      # centrar título
    )
    st.plotly_chart(fig_vote, use_container_width=True)

with cols[4]: #.container(border=True, height="stretch"):
    lang_counts = df_popular['original_language'].value_counts().reset_index()
    lang_counts.columns = ['language','count']
    fig_lang = px.bar(lang_counts, x='language', y='count',
                      title="Movies by Original Language",
                      color_discrete_sequence=[COLOR_KPI])
    # Centrar el título
    fig_lang.update_layout(
        title={
            'text': "Popularity Distribution",
            'x': 0.5,           # centro horizontal
            'xanchor': 'center',
            'yanchor': 'top'
        },
        width=600,       # ancho de la figura
        height=350,      # alto de la figura
        bargap=0.2,      # espacio entre barras
        title_x=0.5      # centrar título
    )
    st.plotly_chart(fig_lang, use_container_width=True)


st.markdown("---")

# -----------------------------
# KPIs: Top Rated Movies
# -----------------------------
st.markdown("### Top Rated Movies Overview")

col1, col2, col3 = st.columns(3)

with col1:
    kpi_with_icon(
        icon_dir / "movies.png",
        "Total Movies",
        kpis_top_rated['total_movies']
    )

with col2:
    kpi_with_icon(
        icon_dir / "polarity.png",
        "Average Popularity",
        f"{kpis_top_rated['avg_popularity']:.1f}"
    )

with col3:
    kpi_with_icon(
        icon_dir / "vote.png",
        "Average Vote",
        f"{kpis_top_rated['avg_vote']:.1f}"
    )

col1, col2, col3 = st.columns([2, 2, 1])
col1.metric("Most Popular Movie", kpis_top_rated['most_popular'])
col2.metric("Highest Rated Movie", kpis_top_rated['highest_rated'])
col3.metric("Movies for Adults", kpis_top_rated['adult_count'])
st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# Top Rated Movies Charts
# -----------------------------
cols = st.columns([1, 0.3, 1, 0.3, 1])

with cols[0]:
    fig_popularity_tr = px.histogram(
        df_top_rated,
        x='popularity',
        nbins=20,
        color_discrete_sequence=[COLOR_KPI]
    )
    
    # Centrar el título
    fig_popularity_tr.update_layout(
        title={
            'text': "Popularity Distribution",
            'x': 0.5,           # centro horizontal
            'xanchor': 'center',
            'yanchor': 'top'
        },
        width=600,       # ancho de la figura
        height=350,      # alto de la figura
        bargap=0.2,      # espacio entre barras
        title_x=0.5      # centrar título
    )
    
    st.plotly_chart(fig_popularity_tr, use_container_width=True)

with cols[2]:
    fig_vote_tr = px.histogram(
        df_top_rated,
        x='vote_average',
        nbins=20,
        color_discrete_sequence=[COLOR_KPI]
    )
    # Centrar título
    fig_vote_tr.update_layout(
        title={
            'text': "Vote Average Distribution",
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        width=600,       # ancho de la figura
        height=350,      # alto de la figura
        bargap=0.2,      # espacio entre barras
        title_x=0.5      # centrar título
    )
    st.plotly_chart(fig_vote_tr, use_container_width=True)

with cols[4]:
    lang_counts_tr = df_top_rated['original_language'].value_counts().reset_index()
    lang_counts_tr.columns = ['language', 'count']
    fig_lang_tr = px.bar(
        lang_counts_tr,
        x='language',
        y='count',
        color_discrete_sequence=[COLOR_KPI]
    )
    # Centrar título
    fig_lang_tr.update_layout(
        title={
            'text': "Movies by Original Language",
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        width=600,       # ancho de la figura
        height=350,      # alto de la figura
        bargap=0.2,      # espacio entre barras
        title_x=0.5      # centrar título
    )
    st.plotly_chart(fig_lang_tr, use_container_width=True)


# -----------------------------
# Dataset Previews
# -----------------------------
st.markdown("### Datasets Previews")

cols = st.columns(2)

with cols[0]:
    st.markdown(
        """
        Top Rated Movies Dataset
        """
    )
    st.dataframe(df_top_rated, use_container_width=True, height=350)

with cols[1]:
    st.markdown(
        """
        Popular Movies Dataset
        """
    )
    st.dataframe(df_popular, use_container_width=True, height=350)



# -----------------------------
# Key Takeaways
# -----------------------------
st.markdown("---")
st.markdown("""
### Key Takeaways
- Popular movies dataset shows which titles are trending and how audience votes are distributed.
- Top rated movies highlight critically acclaimed films with high average votes.
- Language distribution gives insight into global production trends.
- The dashboards are interactive; explore the histograms and bar charts for detailed insights.
""")
