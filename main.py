
# this is without import csv
# with open("weather_data.csv") as data:
#     weather_list = data.readlines()
#     print(weather_list)
# --------------------------------------

#this is with csv imported
# import csv
# with open("weather_data.csv") as data:
#     weather_data = csv.reader(data)
#     print(weather_data)
#     temperatures = []
#     for row in weather_data:
#         if row[1] != "temp":
#             temperature_data = int(row[1])
#             temperatures.append(temperature_data)
#     print(temperatures)
# --------------------

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)