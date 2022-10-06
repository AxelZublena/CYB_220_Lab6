# 9.3
class User():

    def __init__(self, first_name, last_name, age, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} is {self.age} years old and is {self.nationality}.")

    def greet_user(self):
        print(f"Hi {self.first_name.title()}! How are you today?")


user1 = User("axel", "zublena", 20, "french")
user2 = User("bob", "lenon", 60, "english")
user3 = User("charles", "leclerc", 23, "monégasque")

users = [user1, user2, user3]

for user in users:
    print("\n")
    user.describe_user()
    user.greet_user()
