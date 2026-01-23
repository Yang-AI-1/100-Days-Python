print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your current age?"))
    if age <= 12:
        print("Pay 5$ at the counter")
    elif age <= 18:
        print("Pay 9$ at the counter")
    else:
        print("Pay 13$ at the counter")
else:
    print("Sorry you have to grow taller before you can ride.")
