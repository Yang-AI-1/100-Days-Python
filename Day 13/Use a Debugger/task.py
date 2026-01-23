import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2  # The break point breaks the code.
        new_item += random.randint(1, 3)  #Adds a random number to the new item variable.
        new_item = maths.add(new_item, item)   # And then you add the new_item to the looping integer.
    b_list.append(new_item)  # The statement exists outside the for loop so it only appends the added new item.
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])


# The threads and variables tab in the debugger.
# The de-bugger is basically for finding whats wrong with the code at specific points.