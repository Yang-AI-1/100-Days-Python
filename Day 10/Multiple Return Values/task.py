def format_name(f_name, l_name):
    # You can use multiple returns in a function to signify the end of the function.
    if f_name == "" or l_name == "":
        return "You did not provide valid input." #This basically tells the function to end early because a condition was met.
    formated_f_name = f_name.title()              #It basically replaces the function with that string of characters and it is displayed when the function is printed.
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
# The return function is for the entire function, once executed it serves as the end of the function.

print(format_name("AnGEla", "YU"))
