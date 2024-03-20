#
# Uzdevums:
# Izmantojot piemēru no pirma uzdevuma, izveidojiet programmu kas atspoguļos laika apstakļus (temperaturu un nokrišņus) pa stundām 
# izmantojot sekojošu datu linku 
# https://api.open-meteo.com/v1/forecast?latitude=56.8&longitude=24.2&hourly=temperature_2m,precipitation&forecast_days=1
# 


import urllib.request
import json

def get_city_information():
    link = f"https://api.open-meteo.com/v1/forecast?latitude=56.8&longitude=24.2&hourly=temperature_2m,precipitation&forecast_days=1"
    
    with urllib.request.urlopen(link) as response:
        data = response.read().decode('utf-8')

    return json.loads(data)

