# Creating a Class
class User:
# Constructors (initializing an object)
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1 #User that your following   
        self.following += 1 # Your own following going up noted by (self)
     
user_1 = User("001", "Eriel")
user_2 = User("002", "Angela")
user_1.follow(user_2)
print(user_1.following)
print(user_2.followers)