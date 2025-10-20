# modules/integration.py
import pandas as pd
import plotly.express as px

def plot_correlation_heatmap():
    df = pd.read_csv("../data_files/integration_metrics.csv")
    fig = px.imshow(
        df.corr(),
        text_auto=True,
        aspect="auto",
        color_continuous_scale="RdBu_r",
        title="Correlation Between Geographic Adoption and Price Volatility"
    )
    fig.update_layout(title_x=0.5)
    return fig
