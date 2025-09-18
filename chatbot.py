class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def options(self):
        print(f"Welcome, {self.name}! How can I help you? \n1: How can I configure my server settings? \n2: How can I change my user settings? \n3: Is there a way I can add people to my server?")






on = True
while on:
    print("Welcome! What is your name?")
    name1 = input()
    print("Now, what is your age?")
    age1 = input()
    user1 = User(name1, age1)
    user1.options()