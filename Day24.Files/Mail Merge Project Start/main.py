#TODO: Create a letter using starting_letter.txt 
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./input/Names/invited_names.txt") as names:
    name_list = names.readlines() #Creates a list of names.

directory = "./Output/ReadyToSend/"
file_names = ["Letter_for_" + name.strip() + ".txt" for name in name_list]

for name_index in range(len(name_list)): #Provides the name index in each loop which maps the new file name and content to replace in the starting_letter.
    with open("./input/Letters/starting_letter.txt") as letter:
        contents_of_letter = letter.read()

    with open(directory + file_names[name_index], "w") as new_file: #Opens a new file with the directory and new name.
        new_file.write(contents_of_letter.replace("[name]", name_list[name_index].strip()))  #In the new file it writes the letter with the name