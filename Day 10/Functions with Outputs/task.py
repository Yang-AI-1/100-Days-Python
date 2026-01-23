def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}" #Printing only displays the outcome but doesn't give an output.
# So the return function basically replaces the function with the output.
# So the variable gets an output that can be used in a different place.
formatted_string = format_name("DYLan","okomol")
print(formatted_string)
