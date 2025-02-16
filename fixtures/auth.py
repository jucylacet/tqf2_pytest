class AuthService:
    def __init__(self):
        self.users = {"user1": "password1", "user2": "password2"}

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        return False
