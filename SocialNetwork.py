from User import User


class SocialNetwork:
    _instance = None

    def __new__(cls, name):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name = name
            cls._instance.users = {}
            print(f"The social network {name} was created!")
        return cls._instance

    def sign_up(self, username, password):
        if len(password) < 4 or len(password) > 8:
            raise ValueError("Password must be between 4 and 8 characters.")

        if username in self.users:
            raise ValueError("Username already exists.")

        user = User(username, password)
        self.users[username] = user
        return user

    def log_in(self, name, password):
        if self.users[name].password == password:
            self.users[name].boolean_log = True
            print(f"{name} connected")
            return True

    def log_out(self, name):
        if self.users.get(name):
            self.users[name].boolean_log = False
            print(f"{name} disconnected")

    def __str__(self):
        print(f"{self.name} social network:")
        for i in self.users:
            print(self.users[i])
        return " "
