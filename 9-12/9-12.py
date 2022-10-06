# 9.12
from admin import Admin

admin = Admin("axel", "zublena", 20, "french", ["can add post", "can delete post", "can ban user", "can access dashboard"])
admin.privileges.show_privileges()
