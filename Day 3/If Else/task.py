print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
# The height is conditional for 120cm
# The greater than means greater than 120(Not including 120)
# To include 120 use greater than or equals to >=  <---- Articulated such as.
if height > 120:
    print("You can buy a ticket")
# The indented(spaced lines) means that the code block is below the if or else statement
else:
    print("Sorry you are not allowed to buy a ticket for this")
