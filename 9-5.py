# 9.5
class User():

    def __init__(self, first_name, last_name, age, nationality, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} is {self.age} years old and is {self.nationality}.")

    def greet_user(self):
        print(f"Hi {self.first_name.title()}! How are you today?")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User("axel", "zublena", 20, "french")

print(user.login_attempts)
print("\n")
for counter in range(9):
    user.increment_login_attempts()
    print(user.login_attempts)

user.reset_login_attempts()
print("\n")
print(user.login_attempts)
