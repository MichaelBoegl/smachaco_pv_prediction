# local_pv_prediction

One or Two sentence description of the package...

## Using

# Home-assistant

## PV Query

```SQL
SELECT * FROM public.states where metadata_id=793
```

# GeoSphere Austria Cheat Sheet

Overview models: https://data.hub.geosphere.at/dataset/?page=1

## Historic Weather Data

klima-v2-10min
klima-v2-1h

## Web-UI 

https://dataset.api.hub.geosphere.at/app/frontend/station/historical/klima-v2-10min
https://dataset.api.hub.geosphere.at/app/frontend/station/historical/klima-v2-1h

## Get all stations

```bash
curl -X 'GET' 'https://dataset.api.hub.geosphere.at/v1/station/historical/klima-v2-1h/metadata/stations' -H 'accept: application/json' 
```
02902,11004,REICHERSBERG,13.376111,48.331112,351.0,2008-06-25,2100-12-31,OOE,ja,ja

16400,11240,GRAZ-FLUGHAFEN,15.44,46.980556,340.0,2010-11-23,2100-12-31,STMK,ja,ja
16412,11290,GRAZ-UNIVERSITAET,15.448889,47.077778,367.0,1992-08-29,2100-12-31,STMK,ja,ja
16413,11238,GRAZ/STRASSGANG,15.410277,47.046112,357.0,2007-11-27,2100-12-31,STMK,ja,ja

## Get all parameters

```bash
curl -X 'GET' 'https://dataset.api.hub.geosphere.at/v1/station/historical/klima-v2-1h/metadata/parameters' -H 'accept: application/json'
```

Parameterkürzel,Kurzbeschreibung,Beschreibung,Einheit,Codelist
cglo,Globalstrahlung Mittelwert,"Globalstrahlung, kalibriert, Mittelwert",W/m²,
cglo_flag,Qualitätsflag für Globalstrahlung Mittelwert,"Qualitätsflag für Globalstrahlung, kalibriert, Mittelwert",code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
chim,Himmelsstrahlung Mittelwert,"Diffusstrahlung, nicht geprüft, kalibriert, Mittelwert",W/m²,
chim_flag,Qualitätsflag für Himmelsstrahlung Mittelwert,"Qualitätsflag für Diffusstrahlung, nicht geprüft, kalibriert, Mittelwert",code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
dd,Windrichtung,"Windrichtung [360°], vektorieller 10-Minuten-Mittelwert",°,
dd_flag,Qualitätsflag für Windrichtung,"Qualitätsflag für Windrichtung [360°], vektorieller 10-Minuten-Mittelwert",code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
ddx,Windrichtung zur Spitzenböe,Windrichtung der maximalen Windgeschwindigkeit (Spitzenböe) [360°],°,
ddx_flag,Qualitätsflag für Windrichtung zur Spitzenböe,Qualitätsflag für Windrichtung der maximalen Windgeschwindigkeit (Spitzenböe) [360°],code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
ff,"Windgeschwindigkeit 10m, vektorieller Mittelwert","Windgeschwindigkeit in 10m Höhe, vektorieller 10-Minuten-Mittelwert",m/s,
ffam,"Windgeschwindigkeit 10m, arithmetischer Mittelwert","Windgeschwindigkeit in 10m Höhe, arithmetischer 10-Minuten-Mittelwert",m/s,
ffam_flag,"Qualitätsflag für Windgeschwindigkeit 10m, arithmetischer Mittelwert","Qualitätsflag für Windgeschwindigkeit in 10m Höhe, arithmetischer 10-Minuten-Mittelwert",code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
ff_flag,"Qualitätsflag für Windgeschwindigkeit 10m, vektorieller Mittelwert","Qualitätsflag für Windgeschwindigkeit in 10m Höhe, vektorieller 10-Minuten-Mittelwert",code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
ffx,Maximale Windgeschwindigkeit (Spitzenböe),"Windgeschwindigkeit in 10m Höhe, 10-Minuten-Maximalwert (Windspitze)",m/s,
ffx_flag,Qualitätsflag für Maximale Windgeschwindigkeit (Spitzenböe),"Qualitätsflag für Windgeschwindigkeit in 10m Höhe, 10-Minuten-Maximalwert (Windspitze)",code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
p,Luftdruck,"Luftdruck, 10-Minuten-Messwert",hPa,
p_flag,Qualitätsflag für Luftdruck,"Qualitätsflag für Luftdruck, 10-Minuten-Messwert",code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
pred,Reduzierter Luftdruck,Reduzierter Luftdruck: berechneter 10-Minutenwert,hPa,
pred_flag,Qualitätsflag für Reduzierter Luftdruck,Qualitätsflag für Reduzierter Luftdruck: berechneter 10-Minutenwert,code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
rf,Relative Feuchte,"Relative Feuchte, 10-Minuten-Messwert",%,
rf_flag,Qualitätsflag für Relative Feuchte,"Qualitätsflag für Relative Feuchte, 10-Minuten-Messwert",code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
rr,Niederschlagssumme,"Niederschlagssumme, berechnet aus 1-Minuten-Niederschlags-Daten",mm,
rr_flag,Qualitätsflag für Niederschlagssumme,"Qualitätsflag für Niederschlagssumme, berechnet aus 1-Minuten-Niederschlags-Daten",code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
rrm,Niederschlagsdauer,"Niederschlagsdauer, berechnet aus 1-Minuten-Niederschlagsmelder-Daten",min,"[{'key': 0, 'value': 'kein Niederschlag gemessen'}, {'key': 1, 'value': 'Niederschlag gemessen'}]"
rrm_flag,Qualitätsflag für Niederschlagsdauer,"Qualitätsflag für Niederschlagsdauer, berechnet aus 1-Minuten-Niederschlagsmelder-Daten",code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
sh,"Gesamtschneehöhe, Schneepegelmessung","Gesamtschneehöhe aus Schneepegelmessung, 10-Minuten-Mittelwert, Offset korrigiert",cm,
sh_flag,"Qualitätsflag für Gesamtschneehöhe, Schneepegelmessung","Qualitätsflag für Gesamtschneehöhe aus Schneepegelmessung, 10-Minuten-Mittelwert, Offset korrigiert",code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
so,Sonnenscheindauer,"Sonnenscheindauer in Sekunden, 10-Minutensumme",s,
so_flag,Qualitätsflag für Sonnenscheindauer,"Qualitätsflag für Sonnenscheindauer in Sekunden, 10-Minutensumme",code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
tb10,Erdbodentemperatur -10cm,"Erdbodentemperatur in 10 cm Tiefe, 10-Minuten-Messwert",°C,
tb10_flag,Qualitätsflag für Erdbodentemperatur -10cm,"Qualitätsflag für Erdbodentemperatur in 10 cm Tiefe, 10-Minuten-Messwert",code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
tb20,Erdbodentemperatur -20cm,"Erdbodentemperatur in 20 cm Tiefe, 10-Minuten-Messwert",°C,
tb20_flag,Qualitätsflag für Erdbodentemperatur -20cm,"Qualitätsflag für Erdbodentemperatur in 20 cm Tiefe, 10-Minuten-Messwert",code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
tb50,Erdbodentemperatur -50cm,"Erdbodentemperatur in 50 cm Tiefe, 10-Minuten-Messwert",°C,
tb50_flag,Qualitätsflag für Erdbodentemperatur -50cm,"Qualitätsflag für Erdbodentemperatur in 50 cm Tiefe, 10-Minuten-Messwert",code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
tl,Lufttemperatur 2m,"Lufttemperatur in 2m Höhe, 10-Minuten-Messwert",°C,
tl_flag,Qualitätsflag für Lufttemperatur 2m,"Qualitätsflag für Lufttemperatur in 2m Höhe, 10-Minuten-Messwert",code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
tlmax,Lufttemperatur 2m Maximalwert,"Lufttemperatur in 2m Höhe, 10-Minuten-Maximalwert",°C,
tlmax_flag,Qualitätsflag für Lufttemperatur 2m Maximalwert,"Qualitätsflag für Lufttemperatur in 2m Höhe, 10-Minuten-Maximalwert",code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
tlmin,Lufttemperatur 2m Minimalwert,"Lufttemperatur in 2m Höhe, 10-Minuten-Minimalwert",°C,
tlmin_flag,Qualitätsflag für Lufttemperatur 2m Minimalwert,"Qualitätsflag für Lufttemperatur in 2m Höhe, 10-Minuten-Minimalwert",code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
ts,Lufttemperatur 5cm,"Lufttemperatur in 5 cm Höhe, 10-Minuten-Messwert",°C,
ts_flag,Qualitätsflag für Lufttemperatur 5cm,"Qualitätsflag für Lufttemperatur in 5 cm Höhe, 10-Minuten-Messwert",code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
tsmax,Lufttemperatur 5cm Maximalwert,"Lufttemperatur in 5 cm Höhe, 10-Minuten-Maximalwert",°C,
tsmax_flag,Qualitätsflag für Lufttemperatur 5cm Maximalwert,"Qualitätsflag für Lufttemperatur in 5 cm Höhe, 10-Minuten-Maximalwert",code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
tsmin,Lufttemperatur 5cm Minimalwert,"Lufttemperatur in 5 cm Höhe, 10-Minuten-Minimalwert",°C,
tsmin_flag,Qualitätsflag für Lufttemperatur 5cm Minimalwert,"Qualitätsflag für Lufttemperatur in 5 cm Höhe, 10-Minuten-Minimalwert",code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"
zeitx,Zeitpunkt der maximalen Windgeschwindigkeit (Spitzenböe),"Zeitpunkt der maximalen Windgeschwindigkeit (Spitzenböe) in 10m Höhe, 10-Minuten-Wert", ,
zeitx_flag,Qualitätsflag für Zeitpunkt der maximalen Windgeschwindigkeit (Spitzenböe),"Qualitätsflag für Zeitpunkt der maximalen Windgeschwindigkeit (Spitzenböe) in 10m Höhe, 10-Minuten-Wert",code,"[{'key': None, 'value': 'undefiniert'}, {'key': 0, 'value': 'ungeprüfte Daten'}, {'key': 10, 'value': 'automatisch geprüft'}, {'key': 11, 'value': 'automatisch geprüft (verändert)'}, {'key': 12, 'value': 'automatisch geprüft (original)'}, {'key': 20, 'value': 'manuell geprüft (unbekannt)'}, {'key': 21, 'value': 'manuell geprüft (verändert)'}, {'key': 22, 'value': 'manuell geprüft (original)'}]"

### Query Historic Station Data

Globalstrahlung und Qualitätswert für Globalstrahlung

```bash
curl -X 'GET' \
  'https://dataset.api.hub.geosphere.at/v1/station/historical/klima-v2-1h?parameters=cglo%2Ccglo_flag&start=2024-07-01T00%3A00&end=2024-07-02T00%3A00&station_ids=159&output_format=geojson' \
  -H 'accept: application/json'
```


## Weather Prediction

### Models

- (nur historisch) INCA: https://data.hub.geosphere.at/dataset/inca-v1-1h-1km
  - Temperatur, Niederschlag, Wind, Globalstrahlung, relative Feuchte, Taupunkt, Luftdruck
  - Auflösung
    - räumlich: 1km
    - zeitlich: 1h
  - Vorhersage wird stündlich neu gerechnet

- AROME: https://data.hub.geosphere.at/dataset/nwp-v1-1h-2500m
  -	Temperatur, Niederschlag, Wind, Globalstrahlung, relative Feuchte, Gewitterindizes, Bewölkung, Druck
  - Auflösung:
    - räumlich: 2,5km
    - zeitlich: 1h
  - Vorhersage für 60 Stunden, wird alle 3 Stunden neu gerechnet

- APOLIS: https://data.hub.geosphere.at/dataset/apolis_short-v1-1d-100m
  - Diffusstrahlung, Direktstrahlung (horizontale Fläche), Direktstrahlung (real geneigte Fläche), Globalstrahlung (horizontale Fläche), Globalstrahlung (real geneigte Fläche), Sonnenscheindauer
  - Auflösung:
    - räumlich: 100m
    - zeitlich: 24h
  - Vorhersage wird täglich für 24 gerechnet

#### Endpunkte

##### nwp - numerical weather prediction


https://dataset.api.hub.geosphere.at/v1/timeseries/forecast/nwp-v1-1h-2500m

curl -X 'GET' \
  'https://dataset.api.hub.geosphere.at/v1/timeseries/forecast/nwp-v1-1h-2500m/metadata' \
  -H 'accept: application/json'

{
  "title": "numerical weather prediction",
  "parameters": [
    {
      "name": "cape",
      "long_name": "Convective available potential energy",
      "desc": "Convectively available potential energy",
      "unit": "m2 s-2"
    },
    {
      "name": "cin",
      "long_name": "Convective inhibition",
      "desc": "Convective inhibition",
      "unit": "J kg-1"
    },
    {
      "name": "grad",
      "long_name": "surface global radiation",
      "desc": "Surface downwelling shortwave is the sum of direct and diffuse solar radiation incident on the surface, and is sometimes called global radiation",
      "unit": "Ws m-2"
    },
    {
      "name": "mnt2m",
      "long_name": "minimum 2m temperature in the last forecast period",
      "desc": "Minimum 2m temperature in the last forecast intervall",
      "unit": "degree Celsius"
    },
    {
      "name": "mxt2m",
      "long_name": "maximum 2m temperature in the last forecast period",
      "desc": "Maximum 2m temperature in the last forecast intervall",
      "unit": "degree Celsius"
    },
    {
      "name": "rain_acc",
      "long_name": "total rainfall amount",
      "desc": "Accumulated total amount of rainfall since start of the forecast",
      "unit": "kg m-2"
    },
    {
      "name": "rh2m",
      "long_name": "relative humidity 2m above ground",
      "desc": "relative humidity 2m above ground",
      "unit": "%"
    },
    {
      "name": "rr_acc",
      "long_name": "total precipitation amount",
      "desc": "Accumulated total amount of liquid and solid precipitation since start of the forecast",
      "unit": "kg m-2"
    },
    {
      "name": "snow_acc",
      "long_name": "total snowfall amount",
      "desc": "Total snowfall amount since start of forecast",
      "unit": "kg m-2"
    },
    {
      "name": "snowlmt",
      "long_name": "snowlimit",
      "desc": "Height above ground where falling snow melts",
      "unit": "m"
    },
    {
      "name": "sp",
      "long_name": "surface pressure",
      "desc": "surface pressure",
      "unit": "Pa"
    },
    {
      "name": "sundur_acc",
      "long_name": "sunshine duration accumulated",
      "desc": "sunshine duration since forecast start",
      "unit": "s"
    },
    {
      "name": "sy",
      "long_name": "weather symbol",
      "desc": "Codes for GeoSphere Austria weather symbol.",
      "unit": "1"
    },
    {
      "name": "t2m",
      "long_name": "2m temperature",
      "desc": "air temperature 2m above ground",
      "unit": "degree Celsius"
    },
    {
      "name": "tcc",
      "long_name": "Total cloud cover",
      "desc": "total cloud cover",
      "unit": "1"
    },
    {
      "name": "u10m",
      "long_name": "10m wind speed in eastward direction",
      "desc": "wind speed in eastward direction",
      "unit": "m s-1"
    },
    {
      "name": "ugust",
      "long_name": "u component of maximum wind gust",
      "desc": "U component of maximum wind gust in the last forecast intervall",
      "unit": "m s-1"
    },
    {
      "name": "v10m",
      "long_name": "10m wind speed in northward direction",
      "desc": "wind speed in northward direction 10m above ground",
      "unit": "m s-1"
    },
    {
      "name": "vgust",
      "long_name": "v compoment of maximum wind gust",
      "desc": "V component of maximum wind gust in the last forecast intervall",
      "unit": "m s-1"
    }
  ],
  "frequency": "1H",
  "type": "timeseries",
  "mode": "forecast",
  "response_formats": [
    "geojson",
    "csv"
  ],
  "last_forecast_reftime": "2025-09-03T06:00+00:00",
  "max_forecast_offset": 5,
  "available_forecast_reftimes": [
    "2025-09-03T06:00+00:00",
    "2025-09-03T03:00+00:00",
    "2025-09-03T00:00+00:00",
    "2025-09-02T21:00+00:00",
    "2025-09-02T18:00+00:00",
    "2025-09-02T15:00+00:00"
  ],
  "forecast_length": 61,
  "bbox": [
    42.981,
    5.498,
    51.81900000000034,
    22.10199999999975
  ],
  "bbox_outer": [
    42.96974998874999,
    5.486749988749989,
    51.83025001125035,
    22.113250011249765
  ],
  "spatial_resolution_m": 2500,
  "crs": "EPSG:4326",
  "grid_bounds": [
    42.981,
    5.498,
    51.81900000000034,
    22.10199999999975
  ]
}


##### ensemble-v1-1h-2500m

https://dataset.api.hub.geosphere.at/v1/timeseries/forecast/ensemble-v1-1h-2500m

curl -X 'GET' \
  'https://dataset.api.hub.geosphere.at/v1/timeseries/forecast/ensemble-v1-1h-2500m/metadata' \
  -H 'accept: application/json'


{
  "title": "ensemble forecast",
  "parameters": [
    {
      "name": "cape_p10",
      "long_name": "Convective available potential energy (10th percentile)",
      "desc": "Convectively available potential energy (10th percentile of an ensemble forecast)",
      "unit": "m2 s-2"
    },
    {
      "name": "cape_p50",
      "long_name": "Convective available potential energy (50th percentile)",
      "desc": "Convectively available potential energy (50th percentile of an ensemble forecast)",
      "unit": "m2 s-2"
    },
    {
      "name": "cape_p90",
      "long_name": "Convective available potential energy (90th percentile)",
      "desc": "Convectively available potential energy (90th percentile of an ensemble forecast)",
      "unit": "m2 s-2"
    },
    {
      "name": "grad_p10",
      "long_name": "surface global radiation (10th percentile)",
      "desc": "Surface downwelling shortwave is the sum of direct and diffuse solar radiation incident on the surface, and is sometimes called global radiation (10th percentile of an ensemble forecast)",
      "unit": "W m-2"
    },
    {
      "name": "grad_p50",
      "long_name": "surface global radiation (50th percentile)",
      "desc": "Surface downwelling shortwave is the sum of direct and diffuse solar radiation incident on the surface, and is sometimes called global radiation (50th percentile of an ensemble forecast)",
      "unit": "W m-2"
    },
    {
      "name": "grad_p90",
      "long_name": "surface global radiation (90th percentile)",
      "desc": "Surface downwelling shortwave is the sum of direct and diffuse solar radiation incident on the surface, and is sometimes called global radiation (90th percentile of an ensemble forecast)",
      "unit": "W m-2"
    },
    {
      "name": "mnt2m_p10",
      "long_name": "minimum 2m temperature in the last forecast period (10th percentile)",
      "desc": "Minimum 2m temperature in the last forecast interval (10th percentile of an ensemble forecast)",
      "unit": "degree Celsius"
    },
    {
      "name": "mnt2m_p50",
      "long_name": "minimum 2m temperature in the last forecast period (50th percentile)",
      "desc": "Minimum 2m temperature in the last forecast interval (50th percentile of an ensemble forecast)",
      "unit": "degree Celsius"
    },
    {
      "name": "mnt2m_p90",
      "long_name": "minimum 2m temperature in the last forecast period (90th percentile)",
      "desc": "Minimum 2m temperature in the last forecast interval (90th percentile of an ensemble forecast)",
      "unit": "degree Celsius"
    },
    {
      "name": "mxt2m_p10",
      "long_name": "maximum 2m temperature in the last forecast period (10th percentile)",
      "desc": "Maximum 2m temperature in the last forecast interval (10th percentile of an ensemble forecast)",
      "unit": "degree Celsius"
    },
    {
      "name": "mxt2m_p50",
      "long_name": "maximum 2m temperature in the last forecast period (50th percentile)",
      "desc": "Maximum 2m temperature in the last forecast interval (50th percentile of an ensemble forecast)",
      "unit": "degree Celsius"
    },
    {
      "name": "mxt2m_p90",
      "long_name": "maximum 2m temperature in the last forecast period (90th percentile)",
      "desc": "Maximum 2m temperature in the last forecast interval (90th percentile of an ensemble forecast)",
      "unit": "degree Celsius"
    },
    {
      "name": "rain_p10",
      "long_name": "rainfall (10th percentile)",
      "desc": "Total amount of rainfall in the last forecast period (10th percentile of an ensemble forecast)",
      "unit": "kg m-2"
    },
    {
      "name": "rain_p50",
      "long_name": "rainfall (50th percentile)",
      "desc": "Total amount of rainfall in the last forecast period (50th percentile of an ensemble forecast)",
      "unit": "kg m-2"
    },
    {
      "name": "rain_p90",
      "long_name": "rainfall (90th percentile)",
      "desc": "Total amount of rainfall in the last forecast period (90th percentile of an ensemble forecast)",
      "unit": "kg m-2"
    },
    {
      "name": "rr_p10",
      "long_name": "precipitation (10th percentile)",
      "desc": "Total amount of liquid and solid precipitation in the last forecast period (10th percentile of an ensemble forecast)",
      "unit": "kg m-2"
    },
    {
      "name": "rr_p50",
      "long_name": "precipitation (50th percentile)",
      "desc": "Total amount of liquid and solid precipitation in the last forecast period (50th percentile of an ensemble forecast)",
      "unit": "kg m-2"
    },
    {
      "name": "rr_p90",
      "long_name": "precipitation (90th percentile)",
      "desc": "Total amount of liquid and solid precipitation in the last forecast period (90th percentile of an ensemble forecast)",
      "unit": "kg m-2"
    },
    {
      "name": "snow_p10",
      "long_name": "total snowfall amount (10th percentile)",
      "desc": "Total snowfall amount in the last forecast period (1h, 10th percentile of an ensemble forecast)",
      "unit": "kg m-2"
    },
    {
      "name": "snow_p50",
      "long_name": "total snowfall amount (50th percentile)",
      "desc": "Total snowfall amount in the last forecast period (1h, 50th percentile of an ensemble forecast)",
      "unit": "kg m-2"
    },
    {
      "name": "snow_p90",
      "long_name": "total snowfall amount (90th percentile)",
      "desc": "Total snowfall amount in the last forecast period (1h, 90th percentile of an ensemble forecast)",
      "unit": "kg m-2"
    },
    {
      "name": "snowlmt_p10",
      "long_name": "snowlimit (10th percentile)",
      "desc": "Height above ground where falling snow melts (10th percentile of an ensemble forecast)",
      "unit": "m"
    },
    {
      "name": "snowlmt_p50",
      "long_name": "snowlimit (50th percentile)",
      "desc": "Height above ground where falling snow melts (50th percentile of an ensemble forecast)",
      "unit": "m"
    },
    {
      "name": "snowlmt_p90",
      "long_name": "snowlimit (90th percentile)",
      "desc": "Height above ground where falling snow melts (90th percentile of an ensemble forecast)",
      "unit": "m"
    },
    {
      "name": "sundur_p10",
      "long_name": "sunshine duration (10th percentile)",
      "desc": "sunshine duration in the last forecast period (10th percentile of an ensemble forecast)",
      "unit": "s"
    },
    {
      "name": "sundur_p50",
      "long_name": "sunshine duration (50th percentile)",
      "desc": "sunshine duration in the last forecast period (50th percentile of an ensemble forecast)",
      "unit": "s"
    },
    {
      "name": "sundur_p90",
      "long_name": "sunshine duration (90th percentile)",
      "desc": "sunshine duration in the last forecast period (90th percentile of an ensemble forecast)",
      "unit": "s"
    },
    {
      "name": "t2m_p10",
      "long_name": "2m temperature (10th percentile)",
      "desc": "air temperature 2m above ground (10th percentile of an ensemble forecast)",
      "unit": "degree Celsius"
    },
    {
      "name": "t2m_p50",
      "long_name": "2m temperature (50th percentile)",
      "desc": "air temperature 2m above ground (50th percentile of an ensemble forecast)",
      "unit": "degree Celsius"
    },
    {
      "name": "t2m_p90",
      "long_name": "2m temperature (90th percentile)",
      "desc": "air temperature 2m above ground (90th percentile of an ensemble forecast)",
      "unit": "degree Celsius"
    },
    {
      "name": "tcc_p10",
      "long_name": "Total cloud cover (10th percentile)",
      "desc": "total cloud cover (10th percentile of an ensemble forecast)",
      "unit": "1"
    },
    {
      "name": "tcc_p50",
      "long_name": "Total cloud cover (50th percentile)",
      "desc": "total cloud cover (50th percentile of an ensemble forecast)",
      "unit": "1"
    },
    {
      "name": "tcc_p90",
      "long_name": "Total cloud cover (90th percentile)",
      "desc": "total cloud cover (90th percentile of an ensemble forecast)",
      "unit": "1"
    },
    {
      "name": "u10m_p10",
      "long_name": "10m wind speed in eastward direction (10th percentile)",
      "desc": "wind speed in eastward direction 10m above ground (10th percentile of an ensemble forecast)",
      "unit": "m s-1"
    },
    {
      "name": "u10m_p50",
      "long_name": "10m wind speed in eastward direction (50th percentile)",
      "desc": "wind speed in eastward direction 10m above ground (50th percentile of an ensemble forecast)",
      "unit": "m s-1"
    },
    {
      "name": "u10m_p90",
      "long_name": "10m wind speed in eastward direction (90th percentile)",
      "desc": "wind speed in eastward direction 10m above ground (90th percentile of an ensemble forecast)",
      "unit": "m s-1"
    },
    {
      "name": "v10m_p10",
      "long_name": "10m wind speed in northward direction (10th percentile)",
      "desc": "wind speed in northward direction 10m above ground (10th percentile of an ensemble forecast)",
      "unit": "m s-1"
    },
    {
      "name": "v10m_p50",
      "long_name": "10m wind speed in northward direction (50th percentile)",
      "desc": "wind speed in northward direction 10m above ground (50th percentile of an ensemble forecast)",
      "unit": "m s-1"
    },
    {
      "name": "v10m_p90",
      "long_name": "10m wind speed in northward direction (90th percentile)",
      "desc": "wind speed in northward direction 10m above ground (90th percentile of an ensemble forecast)",
      "unit": "m s-1"
    }
  ],
  "frequency": "1H",
  "type": "timeseries",
  "mode": "forecast",
  "response_formats": [
    "geojson",
    "csv"
  ],
  "last_forecast_reftime": "2025-09-03T00:00+00:00",
  "max_forecast_offset": 3,
  "available_forecast_reftimes": [
    "2025-09-03T00:00+00:00",
    "2025-09-02T12:00+00:00",
    "2025-09-02T00:00+00:00",
    "2025-09-01T12:00+00:00"
  ],
  "forecast_length": 61,
  "bbox": [
    42.981,
    5.498,
    51.81900000000034,
    22.10199999999975
  ],
  "bbox_outer": [
    42.96974998874999,
    5.486749988749989,
    51.83025001125035,
    22.113250011249765
  ],
  "spatial_resolution_m": 2500,
  "crs": "EPSG:4326",
  "grid_bounds": [
    42.981,
    5.498,
    51.81900000000034,
    22.10199999999975
  ]
}

