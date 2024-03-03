from User import User


# Regarding design patterns We used the social network in Sillington to make sure there was only one instance of a social network
# We used the posts factory to classify the different types of posts so that each type of post has its appropriate methods
# We used Observer in notifications to keep all followers up to date with what you're doing
class SocialNetwork:
    _instance = None

    def __new__(cls, name):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name = name
            cls._instance.users = {}
            print(f"The social network {name} was created!")
        return cls._instance

    # User registration function. Checking that there is no similar username and password between 4-8
    def sign_up(self, username, password):
        if len(password) < 4 or len(password) > 8:
            raise ValueError("Password must be between 4 and 8 characters.")

        if username in self.users:
            raise ValueError("Username already exists")

        user = User(username, password)
        self.users[username] = user
        return user

    # Login function. Checking that the username really exists and that this is really his password
    def log_in(self, username, password):
        if username not in self.users:
            raise ValueError("User does not exist")
        user = self.users.get(username)
        if user and user.password == password:
            user.boolean_log = True
            print(f"{username} connected")
            return True
        else:
            print("Invalid username or password.")
            return False

    # Function to disconnect from the network. Checking that the username is really connected, and if so, then making
    # it offline
    def log_out(self, name):
        if not self.users.get(name).is_connected:
            raise ValueError("You are not connected to the social network")
        if self.users.get(name):
            self.users[name].boolean_log = False
            print(f"{name} disconnected")

    # A function that prints all the details of the network
    def __str__(self):
        str1 = f"{self.name} social network:\n"
        for i, user in enumerate(self.users):
            str1 += f"{str(self.users[user])}"
            str1 += "\n"
        return str1
