# 9.12
from user import User
from privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, age, nationality, privileges):
        super().__init__(first_name, last_name, age, nationality)
        self.privileges = Privileges(privileges) 
