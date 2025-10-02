import streamlit as st
from datetime import datetime, timedelta, UTC
import pandas as pd
from pickle import load
import requests
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import ephem
import numpy as np
import torch

from backend import *

st.set_page_config(
    page_title="SmaChaCo - Photovoltaik Energieprognose",
    page_icon="🌤️",
    layout="wide"

)
st.title("SmaChaCo - Photovoltaik Energieprognose")

dt_start = datetime.now(tz=UTC)
dt_end = dt_start + timedelta(hours=60)

config = {
    "lat": "47.0835805720088",
    "lon": "15.41304765317576",
    "elev": 353 
}

model_infos = [
    ('wr1', 'torch', 'st_pv_prediction/models/torch_regression_w1.torch'),
    ('wr2', 'torch', 'st_pv_prediction/models/torch_regression_w2.torch'),
    ('wr3', 'torch', 'st_pv_prediction/models/torch_regression_w3.torch'),
    ('wr4', 'torch', 'st_pv_prediction/models/torch_regression_w4.torch'),
    ('wr5', 'torch', 'st_pv_prediction/models/torch_regression_w5.torch'),
]
print("load model...", end="")
models = load_models(model_infos)
print("ok")

print("load marketdata...", end="")
mp_df = get_marketdata()
print("ok")

print(mp_df)

print("load prediction...", end="")
cglo_df = get_cglo_prediction(config, dt_start, dt_end)
print("ok")

print(cglo_df)

print(cglo_df['timestamp'].values)

print("get sun positions...", end="")
sun_df = get_sun_position(config, cglo_df['timestamp'])
print("ok")

print(sun_df)

print("merge feature dataframes...", end="")
m_df = cglo_df.merge(sun_df, how='inner', left_on='timestamp', right_on='timestamp')
print("ok")

print(m_df)

print("get pv prediction...", end="")
p_df = get_pv_predictions(models, m_df)
print("ok")

p_df = p_df.merge(mp_df, how='left', left_on='timestamp', right_on='timestamp')
print(p_df)

st.markdown("# Prognose PV-Output")

st.markdown(f"Erstellzeitpunkt: {dt_start.strftime("%Y-%m-%d %H:%M")}")

fig = make_subplots(specs=[[{"secondary_y": True}]])

for m in models:
    fig.add_trace(
        go.Scatter(x=m_df['timestamp'], y=p_df[m], name=f"Wechselrichter {m}"),
        secondary_y=False
    )

fig.add_trace(
    go.Scatter(x=m_df['timestamp'], y=p_df['cglo'], name="Prognose Globalstrahlung"),
    secondary_y=False
)

fig.add_trace(
    go.Scatter(x=m_df['timestamp'], y=p_df['price'], name="Strompreis Euro/kWh"),
    secondary_y=True
)
fig.update_layout(
    title_text = "Prognose PV-Output"
)

fig.update_xaxes(title_text="Datum und Uhrzeit")
fig.update_yaxes(title_text="Output [Wh] / Globalstrahlung [W/m^2]", secondary_y=False)
fig.update_yaxes(title_text="Marktpreis [€/kWh]", secondary_y=True)
st.write(fig)

properties = ['timestamp']
properties += models.keys()

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("# Stundenübersicht")
    hourly_df = p_df[properties].set_index('timestamp').resample('h').sum().reset_index()
    hourly_df = hourly_df.rename(columns={'cglo': 'Globalstrahlung', 'timestamp': 'Zeitpunkt'})
    fig = px.bar(data_frame=hourly_df, x='Zeitpunkt', y=[x for x in models.keys()])
    st.write(fig)

with col2:
    st.markdown('# Tagesübersicht')
    daily_df = p_df[properties].set_index('timestamp').resample('D').sum().reset_index()
    daily_df = daily_df.rename(columns={'cglo': 'Globalstrahlung', 'timestamp': 'Zeitpunkt'})
    fig = px.bar(data_frame=daily_df, x='Zeitpunkt', y=[x for x in models.keys()])
    st.write(fig)

properties = ['timestamp', 'cglo']
properties += models.keys()
properties += ['price']

st.markdown("# Tabellenansicht")
m_df = p_df[properties].rename(columns={'cglo': 'Globalstrahlung', 'timestamp': 'Zeitpunkt', 'price': 'Marktpreis'})
st.download_button("Download Data", m_df.to_csv(index=False).encode("utf-8"), "forecast.csv", "text/csv", key="download-csv")
st.dataframe(m_df)

