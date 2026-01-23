def format_name(f_name, l_name):
    #Multiple lines of cov strings can be written.
    #The computer interprets them as comments so it doesent print them out.
    """This function returns arguments that
    have been converted to title case. """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")
length = len(formatted_name)

print(formatted_name)

