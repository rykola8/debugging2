#
# Uzdevums:
# - salabot kodu
# - pievienot papildus informācijas atspoguļošanu par pilsētu: populācija, laika josla un valsts kods
# - pievienot validāciju: pārbaudīt ka ievadītā pilsēta ir vismaz 2 simboli
# - pamainīt API tāda veidā lai rezultāti tiktu atgriezti latviešu valodā
#

import urllib.request
import json

def get_city_information(city):
    link = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=3&language=en&format=json"
    
    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8')

    return json.loads(data)

def display_city_information(city_info):
    if city_info
        print("City Information:")
        for city_data in city_info['results']:
            print(f"Name: {city_data['name']}")
            print(f"Country: {city_data['county']}")
            print(f"Latitude: {city_data['lat']}")
            print(f"Longitude: {city_data['lon']}")
            print("-----------------------")
    else:
        print("No city information available.")

city_name = input("Enter city name: ")
city_information = get_city_information(city_name)
display_city_information(city_information)
