print("welcome to the tip calculator!")
a = float(input("What was the total bill?"))
b = int(input("How much would you like to give? 10,12 or 15 percent?"))
c = int(input("How many people are to split the bill"))
d = a*(b / 100 + 1)/ c
print(f"Each person should pay: ${d}")


