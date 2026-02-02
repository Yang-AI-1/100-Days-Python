# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()  #Readline = singular. Readlines = plural.
#     print(data)

# import csv
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

import pandas


data = pandas.read_csv("weather_data.csv")
print(data)

temp_list = data["temp"].to_list()

# average = sum(temp_list) / len(temp_list)
# print(average.__round__(2))

temp_mean = data["temp"].mean()
max_temp = data["temp"].max()

print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
print(monday.temp * 9/5 +32)



