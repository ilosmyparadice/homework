import json
import csv

with open("city.list.json", "r", encoding="utf-8") as f:
    data = json.load(f)

#1
print("Количество городо в файле: ", len(data))

#2
emptydict = {}
for city in data:
    if city["country"] not in emptydict:
        emptydict[city["country"]] = 1
    else:
        emptydict[city["country"]] += 1

print("=" * 50)
print(emptydict)

#3
countfornorth = 0
countforsouth = 0
countforequator = 0
for city in data:
    if city["coord"]["lat"] > 0:
        countfornorth += 1
    elif city["coord"]["lat"] == 0:
        countforequator += 1
    else: countforsouth += 1

print("=" * 50)
print(f"Количество городов на севере: {countfornorth}\nКоличество городов на юге: {countforsouth}\nКоличество городов на экваторе: {countforequator}")

#4
with open("city.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter="|")
    writer.writerow(["name", "country", "coordinates"])

    for city in data:
        name = city["name"]
        country = city["country"]
        coordinates = f'{city["coord"]["lat"]},{city["coord"]["lon"]}'
        writer.writerow([name, country, coordinates])

#5
filtred = []
for city in data:
    if city["country"] == "RU":
        filtred.append(city)

with open("cityru.json", "w", encoding="utf-8") as f:
    json.dump(filtred, f)

#6

countries = {}

for city in data:
    country = city["country"]
    if country not in countries:
        countries[country] = []
    countries[country].append(city)

for country_code, cities in countries.items():
    filename = f"{country_code}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(cities, f)











