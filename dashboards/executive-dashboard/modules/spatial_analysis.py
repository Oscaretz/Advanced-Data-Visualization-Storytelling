# modules/spatial_analysis.py
import pandas as pd
import plotly.express as px

def plot_geo_interest():
    df = pd.read_csv("../data_files/google_trends.csv")
    fig = px.choropleth(
        df,
        locations="country",
        locationmode="country names",
        color="interest_score",
        color_continuous_scale="Viridis",
        title="Global Interest in Cryptocurrencies (Google Trends)"
    )
    fig.update_layout(title_x=0.5)
    return fig
