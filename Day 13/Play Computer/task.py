year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
# elif year > 1994:  <--- The bug
elif year >= 1994:   # <---- The number.
    print("You are a Gen Z.")
# ^ In the above code 1994 hasn't been factored anywhere because of improper use on inequalities.

#Think as a computer in a true false manner.