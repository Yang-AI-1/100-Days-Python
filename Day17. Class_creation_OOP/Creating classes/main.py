class User:  #<---- A class used to model users of lets say a website.
    #This is called the constructor.
    def __init__(self, user_id, username):  #This is where we initialise or create starting values. # We can add parameters to the initialising function to aid in modifying the attributes of the object.
        """ Innit functions will always be called every time you create a new user."""
        self.id = user_id #<--- We're basically saying that the object.id is the parameter user_id, that will take the argument equal to a user id.
        self.username = username
        self.followers = 0  #This is an example of setting an initial attribute that all the objects have in common.
        self.following = 0

    def follow(self, user): # Following someone serves as a method, the user being followed is passed in as a parameter.

        user.followers += 1 #This means that the user who we are following have their counts go up by 1
        self.following += 1  # The self means that our following goes up by one as well.
        # The self is a way for us to refer to the users.



user_1 = User("001", "Dylan")  #An object of a user has been created.


print(user_1.username)

#It's just like assigning variables.
