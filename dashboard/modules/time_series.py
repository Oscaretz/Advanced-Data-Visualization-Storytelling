# modules/time_series.py
import pandas as pd
import plotly.express as px

def plot_random_walk_analysis():
    df = pd.read_csv("../data_files/crypto_prices.csv")
    df['date'] = pd.to_datetime(df['date'])
    
    fig = px.line(
        df,
        x="date",
        y="price",
        color="crypto",
        title="Cryptocurrency Price Evolution (Random Walk Check)"
    )
    fig.update_layout(
        template="plotly_white",
        title_x=0.5,
        font=dict(family="Inter", size=14)
    )
    return fig
