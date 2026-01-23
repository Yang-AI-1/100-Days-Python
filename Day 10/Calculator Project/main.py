# TODO. Write out the calc functions.
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


# TODO. add the 4 functions into a dictionary.

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide}
# Dictionaries can be arranged in multiple lines.

# TODO. Use the dictionary operations to perform the calculations.

# first_number = int(input("Type the first number: ")) #Data type integer
# second_number = int(input("Type the second number: "))
# chosen_operation = input("Choose your operation:") #Data type string = Dictionary key.
import art
Calculating = True
while Calculating:
    print(art.logo)
    first_number = float(input("Type the first number: "))
    Calculating2 = True
    while Calculating2:
        for key in operations:
            print(key)
        chosen_operation = input("Choose your operation:") #Rember to edit it so that if someone chooses a wrong logical operator it breaks the function.
        second_number = float(input("Type the second number: "))
        total_value = operations[chosen_operation](first_number,second_number)
        calculated_value = total_value
        print(f"{first_number} {chosen_operation} {second_number} = {calculated_value}")
        decision = input(f"Type 'y' to continue with {calculated_value} or type 'n' to start a new operation.").lower()
        if decision == "n":
            Calculating2 = False
            print("\n" * 100)
        elif decision == "y": #Figure out a way to make the first number the calculated value
            first_number = calculated_value
# Can continue to be improved according to user experience.