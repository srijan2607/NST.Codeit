# air_quality = {"delhi" : 500, "Sonipat": 200, "Mumbai":180, "Pune" :134}
# for city in air_quality:
#     print(city, ":" ,air_quality[city])

# for city in air_quality.keys():
#     print(city)
# for aqi in air_quality.values():
#     print(aqi)
# for value in air_quality.items():
#     print(value)
# for city,aqi in air_quality.items():
#     print(city, ":" ,aqi)

# cars = {
#     "SUV" : {"Defender": "1.5cr", "Urus" : "3cr"},
#     "Hatchback" : {"Maruti" : "2.5cr", "Honda" : "2.8cr"},
#     "Sedan" : {"Toyota" : "3.2cr", "Hyundai" : "2.7cr"},
# }
# print(cars["SUV"])

vs = {x : x **2 for x in range(1,11) if x % 2 != 0}
print(vs)