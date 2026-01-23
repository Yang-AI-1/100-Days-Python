letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = " "
import random
# In this context the range function is giving us the freedom to choose the number of iterations of the loop.
# Unless the assigned variables of the for range are being used for certain functions, the range can be equal to the number of required loop iterations.
for char in range(nr_letters):
    random_char = random.choice(letters)
    password += random_char
for number in range(nr_numbers ):
    random_numb = random.choice(numbers)
    password += random_numb
for symbol in range(nr_symbols):
    random_symb = random.choice(symbols)
    password += random_symb

pass_l = list(password)
random.shuffle(pass_l)
secure_pass = ''.join(pass_l)

print(secure_pass)
# Always print the final result.Unless you wanted something to be printed in loops.