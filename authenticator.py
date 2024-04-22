from user import User

class Authenticator:
    def __init__(self):
        self.users = []

    def add_user(self, username, password):
        self.users.append(User(username, password))

    def login(self, username, password):
        for user in self.users:
            if user.verify_credentials(username, password):
                return True
        return False
