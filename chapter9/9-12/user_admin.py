from user import Users

class Privileges():
    def __init__(self):
        self.privileges = ["add user", "remove user", "change user", "edit user"]
    
    def show_privileges(self):
        print("The Admin user has the following privileges:")
        for privilege in self.privileges:
            print(f"\t-{privilege}")

class Admin(Users):
    def __init__(self, first_name, last_name, password="password", subscription="basic"):
        super().__init__(first_name, last_name, password, subscription)
        self.privileges = Privileges()