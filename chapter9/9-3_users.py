class Users():
    def __init__(self, first_name, last_name, password, subscription):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.subscription = subscription

    def describe_user(self):
        print("\nUser information:- ")
        print(f"\tFirst name: {self.first_name}")
        print(f"\tLast name: {self.last_name}")
        print(f"\tPassword: {self.password}")
        print(f"\tSubscription: {self.subscription}")

    def greet_user(self):
        print(f"\nWelcome {self.first_name}!")


karissa = Users("Karissa", "Tysklind", "badpassword", "Basic")
cynthia = Users("Cynthia", "Karimi", "bad`password", "Premum")
ammar = Users("Ammar", "Karimi", "badpassword", "Family")

ammar.describe_user()
cynthia.describe_user()
karissa.describe_user()

ammar.greet_user()
cynthia.greet_user()
karissa.greet_user()
