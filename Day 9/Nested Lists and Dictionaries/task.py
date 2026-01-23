travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
#Retrieving a specific item from a nested list.
print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]] #A list within a list. My guess is that the list occupies one index of the original list.
#The nested list item retrieval. First list index then nested list index.Different brackets.
print(nested_list[2][1])
#You can nest a list inside a nested dictionary.
# Retrieving data from such nesting.
# print(travel_log["Germany"]["cities_visited"][2])