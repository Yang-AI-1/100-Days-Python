programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",     #This sort of arrangement is for neatness purposes.
}
# To retrieve a value out of a dictionary you print the dictionary variable with the specific key bracketed.
print(programming_dictionary["Bug"]) #It prints the value(String) itself not in the python dictionary format.

# Be careful to:
    #1.Provide the key in its actual data type.
    #2.Spell the key properly while printing it.

programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary) #Printing the entire dictionary prints it in dictionary format.

# #Wipe dictionary:
# programming_dictionary = {} # At this hierarchal stage the programming dictionary is now empty.
# print(programming_dictionary)

#Edit a dictionary. Using an existing key and assigning it to a new value.
programming_dictionary["Bug"] = "A moth in your computer."

# Loop through a dictionary.For loops.
for key in programming_dictionary:
    print(key) #It only loops through the keys in the dictionary.
    print(programming_dictionary[key])  #Putting it in this format allows the values of the keys to be retrieved and printed.

