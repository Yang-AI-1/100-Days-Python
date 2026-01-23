from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"] #Always remember that indexes from a list start from 0.
dice_num = randint(0, 5) #The randint function shows.
print(dice_images[dice_num])

# Reproducing the bug.
# If we can get the error to appear consistently we know what the problem is. Knowing the problem is half fixing it.

# print(dice_images[6]) This is what causes the bug UI to trigger.
# Indexed in a list start from 0. Always remember that.