import os
import time
import random

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class User:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def options(self):
        print(f"Welcome to the Texas Dept. of Information Resources, {self.city} branch(Austin Technology Services)")
        print("1: My technology isnt working. \n2: I think I got hacked. \n3: My Wifi is down.")

    def option1(self):
        print("What type of device are you having issues with? \n 1: Laptop \n 2: Dekstop Computer \n 3: Mobile/Cellular Device \n 4: Other")
        option_device = input("I am having issues with: ")
        match option_device:
            case "1":
                clear_terminal()
                print("Okay. Can you state your issue? \n 1: Will not connect to the web/internet \n 2: Bluetooth does not work")
                issue_laptop = input("I am having issues with: \n ")
                match issue_laptop:
                    case "1":
                        print("Alright! can you enter your laptops 4-digit Serial ID?")
                        laptop_id = input("My Laptops' ID is: ")
                        while(True):
                            if(len(laptop_id) != 4 or laptop_id.isdigit() == False):
                                laptop_id = input("Your laptop ID is invalid. Please re-enter a valid, 4 digit ID: ")
                            if(len(laptop_id) == 4 and laptop_id.isdigit() == True):
                                break 
                        print("Alright! Lets read your laptops data...")
                        time.sleep(2)
                        random_integer = random.randint(0, 3)
                        random_integertwo = random.randint(4, 27)
                        if(int(laptop_id[random_integer]) > 5):
                            print("We see no issue. Your computer seems to be functioning fine. \nWe reccomend checking all cable connections")
                        if(int(laptop_id[random_integer]) <= 5):
                            print(f"We have identified an issue. \nYour ISP has sent out a warning that your general area has had an outage for approx. {random_integertwo} minutes.")
                    case "2":
                        print("Alright! can you enter your laptops 4-digit Serial ID?")
                        laptop_id = input("My Laptops' ID is: ")
                        while(True):
                            if(len(laptop_id) != 4 or laptop_id.isdigit() == False):
                                laptop_id = input("Your laptop ID is invalid. Please re-enter a valid, 4 digit ID: ")
                            if(len(laptop_id) == 4 and laptop_id.isdigit() == True):
                                break 
                        print("Alright! Lets read your laptops data...")
                        time.sleep(2)
                        random_integer = random.randint(0, 3)
                        if(int(laptop_id[random_integer]) > 5):
                            print("We have noticed an issue. You have the improper and/or outdated bluetooth drivers.\n Please install the new drivers through your laptop brands' customer support.")
                        if(int(laptop_id[random_integer]) <= 5):
                            print("It seems the current operating system you are on has some conflicts with bluetooth functionality. \nPlease wait for an updated from the official provider and/or developer of your operating system.")
            case "2":
                clear_terminal()
                print("Okay. Can you state your issue? \n 1: Issue with graphics/screen issues \n 2: Peripheals do not work properly")
                issue_computer = input("I am having issues with: \n ")
                match issue_computer:
                    case "1":
                        print("Alright! can you enter your computers 7-digit Serial ID?")
                        laptop_id = input("My Computer' ID is: ")
                        while(True):
                            if(len(laptop_id) != 7 or laptop_id.isdigit() == False):
                                laptop_id = input("Your laptop ID is invalid. Please re-enter a valid, 7 digit ID: ")
                            if(len(laptop_id) == 7 and laptop_id.isdigit() == True):
                                break 
                        print("Alright! Lets read your computers data...")
                        time.sleep(2)
                        random_integer = random.randint(0, 6)
                        if(int(laptop_id[random_integer]) > 5):
                            print("It seems your graphics card drivers are outdated. \nPlease attempt to instal the newest drivers availble for your graphics card.")
                        if(int(laptop_id[random_integer]) <= 5):
                            print("After attempting to ping and connect with your graphics card, we have not been able to recieve a response. \nIt seems there is a detrimental issues with the graphics card. Please check any cables, or attempt repairs.")
                    case "2":
                        print("Alright! can you enter your computers 7-digit Serial ID?")
                        laptop_id = input("My Computer' ID is: ")
                        while(True):
                            if(len(laptop_id) != 7 or laptop_id.isdigit() == False):
                                laptop_id = input("Your laptop ID is invalid. Please re-enter a valid, 7 digit ID: ")
                            if(len(laptop_id) == 7 and laptop_id.isdigit() == True):
                                break 
                        print("Alright! Lets read your computers data...")
                        time.sleep(2)
                        random_integer = random.randint(0, 6)
                        if(int(laptop_id[random_integer]) > 5):
                            print("We are not recieving any signal from the address, from any sort of peripheal from your I/O. Please check connections.")
                        if(int(laptop_id[random_integer]) <= 5):
                            print("It seems your drivers are outdated. Please try installing new drivers.")
                
                        


                            
                        

                        





     

on = True
while on:
    print("Welcome! What is your name?")
    name1 = input()
    print("Now, what is your age?")
    age1 = input()
    print("What is your city?")
    city1 = input()
    user1 = User(name1, age1, city1)
    user1.options()
    option = input("Which is the issue? ")
    match option:
        case "1":
            user1.option1()
            break
            