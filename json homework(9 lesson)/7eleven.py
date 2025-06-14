import json


with open("city.list.json", "r", encoding="utf-8") as f:
    data = json.load(f)

country_code = "BY"
filtred = []
for city in data:
    if city["country"] == country_code:
        filtred.append(city)

filtred = filtred[:100]

geojson = {
    "type": "FeatureCollection",
    "features": []
}

for city in filtred:
    feature = {
        "type": "Feature",
        "id": "cityID",
        "geometry": {
            "type": "Point",
            "coordinates": [city["coord"]["lon"], city["coord"]["lat"]]
        },
        "properties": {
            "iconCaption": city["name"],
            "marker-color": "b51eff",
        }
    }
    geojson["features"].append(feature)


filename = f"{country_code}.geojson"
with open(filename, "w", encoding="utf-8") as f:
    json.dump(geojson, f)

