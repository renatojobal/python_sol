import json
import urllib.request
from datetime import datetime 
  
  


def to_readable_date(str_time : str):
  """
  Funcion que formate el tiempo y lo imprime de forma legible
  """
  readble_date = datetime.fromtimestamp(str_time).strftime("%Y-%m-%d %H:%M:%S")
  return str(readble_date)

# Descarga de objeto json sin formato
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson"
data = urllib.request.urlopen(url).read().decode()

# Analizar objeto json
obj = json.loads(data)

for i in obj['features']:
  print(i['properties']['title'])
  print("\tMagnitud: %f" % (i['properties']['mag']))
  print("\tTiempo: %s" % (to_readable_date(i['properties']['time']/1000)))
  print("\tLugar: %s" % (i['properties']['place']))
  print('\n')
  
  
