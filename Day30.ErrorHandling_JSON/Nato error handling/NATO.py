# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO1.Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO2.Create a list of the phonetic code words from a word that the user inputs.

#This is the updated error handling one.

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Input only letters in the alphabet.")
        generate_phonetic()
    else:
        return output_list

print(generate_phonetic())
