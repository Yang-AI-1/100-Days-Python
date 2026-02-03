student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
#  {new_key:new_value for (index, row) in df.iterrows()}


#TODO 1. Create a dictionary in this format:
Nato_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv") #If the data is already interpreted your supposed to read it.
Nato_phonetic_dict = {row.letter:row.code for (index, row) in Nato_dataframe.iterrows()}
#iterrows() returns a tuple.Containing the index and the row. It's important to provide two arguments to assign each tuple a value.

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_name = input("Enter name:").upper()
letter_list = [letter for letter in user_name]

Nato_name = [Nato_phonetic_dict[letter] for letter in letter_list]
# Nato_name = [Nato_phonetic_list.get(letter) for letter in user_name if letter.isalpha()] Clearner code to deal with spaces which return none and .isalpha() to check for alphabet letters.
print(Nato_name)

# revisions:
# 1.Nato_phonetic_dict[letter] accesses the value directly. So your looping through the letters and returning the value.
# 2.Initially I was looping through the dictionary. Like this. [code for (letter,code) in Nato_phonetic_dict.items() if letter in letter_list]
# The above code loops through the key value pairs and then checks if the key is in the letter list. This makes it print in alphabetical order.

#Everything really just boils down to what you want with the code.
