class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

    def __repr__(self):
        return f"<User {self.username}>"

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email
        }

    @staticmethod
    def from_dict(data):
        return User(
            user_id=data.get("user_id"),
            username=data.get("username"),
            email=data.get("email")
        )