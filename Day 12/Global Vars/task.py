# Modifying Global Scope.

enemies = 1

# TODO. It is usually a terrible idea to name local variables the same as global variables. Its just creating new variables.
def increase_enemies(enemy):
    #TODO. The global operator allows us to modify global variables. It gets confusing and creates bugs and errors.
    # TODO.it is not advisable to always modify global variables. Instead use assign the function to take a variable and use arguments to execute the code.
    print(f"enemies inside function: {enemies}")
    return enemy + 1
    # ^ The return statement allows the number of enemies to be increased by one. And enemies can be placed as an argument and increased by the return statement.

enemies = increase_enemies(enemy=enemies) #This means that the parameter enemy, has enemies as its key word argument. It'll use that value in the mathematical calculation and return the desired modified value.
print(f"enemies outside function: {enemies}")




