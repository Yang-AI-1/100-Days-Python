
def add(*args):
    return sum(args)

def add_2(*args):
    """Loops through the arguments and adds them."""
    sum = 0 #Setting a variable that's in local scope and mutable.
    for n in args:
        sum += n
    return sum

def calculate(n,**kwargs): #**kwargs just means many key word arguments. Can be along-side a normal parameter
    n += kwargs["add"] #The add and multiply are the key word arguments the user will pass in
    n *= kwargs["multiply"]
    print(n)

calculate(14,add=2,multiply=3)
#I must pass in n, the arguments must be in keyword form.
#Pycharm detects the use in the function and suggests the keyword arguments to pass in. (How did people used to function without pycharm??!O_O)


print(add(1,2,3,4,5,6,7,8,8,10,11,12,13))

#**kwargs can also apply to classes.

class Car:
    def __init__(self,**kw): #We can just call it kw.
        self.model = kw.get("model")
        self.speed = kw.get("speed")