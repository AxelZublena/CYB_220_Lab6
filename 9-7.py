# 9.7
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


class Admin(User):
    def __init__(self, first_name, last_name, age, nationality, privileges):
        super().__init__(first_name, last_name, age, nationality)
        self.privileges = privileges

    def show_privileges(self):
        print(f"{self.first_name.title()} has the following privileges: ")
        for privilege in self.privileges:
            print(f" - {privilege}")



admin = Admin("axel", "zublena", 20, "french", ["can add post", "can delete post", "can ban user", "can access dashboard"])
admin.show_privileges()
