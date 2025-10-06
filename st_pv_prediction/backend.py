import json
import requests
from datetime import datetime, timedelta, UTC
import pandas as pd
import ephem
import torch
import numpy as np

def get_marketdata():
    api_url = "https://api.awattar.at/v1/marketdata"
    data = None
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()

    timestamps = [datetime.fromtimestamp(x['start_timestamp']/1000, tz=UTC) for x in data['data']]
    market_price = [float(x['marketprice'])/1000 for x in data['data']]
    units = ["Euro/kWh" for x in data['data']]

    p_df = pd.DataFrame({'timestamp': timestamps, 'price': market_price, 'unit': units})
    p_df = p_df.set_index("timestamp").resample("15min").ffill().reset_index()
    return p_df


def get_cglo_prediction(config, dt_start, dt_end):
    point_parameters = {
    "parameters": "grad",
    "lat_lon": f"{config['lat']},{config['lon']}",
    "forecast_offset": 0,
    "start": str(dt_start),
    "end": str(dt_end),
    "output_format": "geojson"
    }

    model_point = 'nwp-v1-1h-2500m'
    api_url = f'https://dataset.api.hub.geosphere.at/v1/timeseries/forecast/'
    query_point = f'{api_url}{model_point}'
    
    timestamps = []
    cglo = []
    response = requests.get(query_point, params=point_parameters)
    if response.status_code == 200:
        data = response.json()
        timestamps = data['timestamps']
        cglo = data['features'][0]['properties']['parameters']['grad']['data']
    else:
        print("  ", response.status_code)

    cglo_df = pd.DataFrame({'timestamp': timestamps, 'cglo': cglo})
    cglo_df['timestamp'] = pd.to_datetime(cglo_df['timestamp'], utc=True)
    cglo_df['cglo'] = cglo_df['cglo'].diff(1)/3600
    cglo_df.loc[cglo_df['cglo']<0, "cglo"] = 0.0
    cglo_df = cglo_df.iloc[1:]

    cglo_df = cglo_df.set_index('timestamp')
    cglo_df = cglo_df.resample("15min").interpolate()
    cglo_df = cglo_df.reset_index()
    return cglo_df


def get_sun_position(config, timestamps):
    o = ephem.Observer()
    o.lat = str(config['lat'])
    o.lon = str(config['lon'])
    o.elev = config['elev']
    o.date = timestamps[0]

    m = ephem.Sun(o)

    dates = []
    alts = []
    azs = []

    dv = {}

    query_dates = timestamps
    for d in query_dates:
        o.date = d

        m.compute(o)
        dates.append(d)
        
        if m.alt >= 0:
            alts.append(m.alt)
            azs.append(m.az)
        else:
            alts.append(0.0)
            azs.append(0.0)
        t = (m.alt, m.az)
        if t not in dv.keys():
            dv[t] = [d]
        else:
            dv[t].append(d)

    
    sun_df = pd.DataFrame(data={"timestamp": dates, "alt": alts, "az": azs})
    #sun_df['datetime'] = pd.to_datetime(sun_df['datetime'], t)
    return sun_df


def load_models(model_info):
    models = {}
    for mi in model_info:
        if mi[1] == "torch":
            m = torch.load(mi[2], weights_only=False)
            models[mi[0]] = dict()
            models[mi[0]]['type'] = mi[1]
            models[mi[0]]['model'] = m
    return models

def get_pv_predictions(models, df):
    print(df)
    X_query = df[['cglo', 'alt', 'az']]
    X_query = torch.tensor(np.asarray(X_query.values).astype('float32'), dtype=torch.float32)
    
    predictons = dict()
    for m in models:
        prediction = models[m]['model'](X_query).detach().numpy()
        df[m] = prediction
    return df
    