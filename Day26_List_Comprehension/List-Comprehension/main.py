numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "Angela"
name_letters = [letter for letter in name]
doubled_range = [n*2 for n in range(1,5)]

names_list = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
long_names = [name.upper() for name in names_list if len(name) > 5]
print(long_names)
