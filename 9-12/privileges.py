# 9.12
class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f"The user has the following privileges: ")
        for privilege in self.privileges:
            print(f" - {privilege}")
