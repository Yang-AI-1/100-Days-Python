#Files can be open read and written using python.
#You do this by using the open() function, .read() and .write() methods.

my_file = open("my_file.txt")  #The file can be stored in a variable.
contents = my_file.read()  #My file is an object and the .read() method retrieves the contents.
print(contents)
my_file.close() #We manually close down the file to save computer resources

#We use the with and as keyword to open and manage the file. We no longer have to close the file manually.
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

#File modes:
#"r" basically just means read only.
#"w" sets it to write, so you can write in the file.This deletes everything in the file and replaces.
#"a" is the append mode. It appends text or whatever, to the file.

#You can create a new file.
with open("/Users/etyan/OneDrive/Desktop/my_file.txt",) as file1: #This is how to use the absolute file path
    contents = file1.read()
    print(contents)

