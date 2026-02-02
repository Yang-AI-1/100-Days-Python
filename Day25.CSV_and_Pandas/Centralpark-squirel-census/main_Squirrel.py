
import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colors = squirrel_data["Primary Fur Color"].unique()
number_per_fur_color = squirrel_data["Primary Fur Color"].value_counts()
# print(fur_colors)
# print(number_per_fur_color)

squirrel_count = pandas.DataFrame(number_per_fur_color).reset_index() #The data has been converted into a dataframe.
squirrel_count.columns = ['Fur Color','Count']
squirrel_count.to_csv("squirrel_count.csv",index= False,)
print(squirrel_count)