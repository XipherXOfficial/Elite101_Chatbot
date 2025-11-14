import os
import time
import random

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class User:
    def __init__(self, name, device):
        self.name = name
        self.device = device

    def options(self):
        print(f"Welcome to the Technology and Device support system, {self.name}. Your registered device currently is {self.device}")
        time.sleep(1)
        print("What type of device are you having issues with? \n 1: Laptop \n 2: Dekstop Computer \n 3: Mobile/Cellular Device")
        option_device = input("I am having issues with: ")
        match option_device:
            case "1":
                clear_terminal()
                print("Okay. Can you state your issue? \n 1: Internal fans arent working properly \n 2: Bluetooth does not work")
                issue_laptop = input("I am having issues with: \n ")
                match issue_laptop:
                    case "1":
                        print(f"Alright! can you enter your {self.device} 4-digit Serial ID?")
                        laptop_id = input(f"My {self.device}' ID is: ")
                        while(True):
                            if(len(laptop_id) != 4 or laptop_id.isdigit() == False):
                                laptop_id = input(f"Your {self.device} ID is invalid. Please re-enter a valid, 4 digit ID: ")
                            if(len(laptop_id) == 4 and laptop_id.isdigit() == True):
                                break 
                        print(f"Alright! Lets read your {self.device}'s data...")
                        time.sleep(2)
                        random_integer = random.randint(0, 3)
                        if(int(laptop_id[random_integer]) > 5):
                            print(f"We see no issue. Your {self.device} seems to be functioning fine. \nWe reccomend checking the internal status of your {self.device}")
                        if(int(laptop_id[random_integer]) <= 5):
                            print(f"We have identified an issue. Your laptops internal fans are not running at the proper power. \nPlease check the power output or other issues with its fans.")
                    case "2":
                        print(f"Alright! can you enter your {self.device} 4-digit Serial ID?")
                        laptop_id = input("My Laptops' ID is: ")
                        while(True):
                            if(len(laptop_id) != 4 or laptop_id.isdigit() == False):
                                laptop_id = input(f"Your {self.device} ID is invalid. Please re-enter a valid, 4 digit ID: ")
                            if(len(laptop_id) == 4 and laptop_id.isdigit() == True):
                                break 
                        print(f"Alright! Lets read your {self.device}'s data...")
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
                        print(f"Alright! can you enter your {self.device} 7-digit Serial ID?")
                        computer_id = input(f"My {self.device}' ID is: ")
                        while(True):
                            if(len(computer_id) != 7 or computer_id.isdigit() == False):
                                computer_id = input(f"Your {self.device} ID is invalid. Please re-enter a valid, 7 digit ID: ")
                            if(len(computer_id) == 7 and computer_id.isdigit() == True):
                                break 
                        print(f"Alright! Lets read your {self.device} data...")
                        time.sleep(2)
                        random_integer = random.randint(0, 6)
                        if(int(computer_id[random_integer]) > 5):
                            print("It seems your graphics card drivers are outdated. \nPlease attempt to instal the newest drivers availble for your graphics card.")
                        if(int(computer_id[random_integer]) <= 5):
                            print("After attempting to ping and connect with your graphics card, we have not been able to recieve a response. \nIt seems there is a detrimental issues with the graphics card. Please check any cables, or attempt repairs.")
                    case "2":
                        print(f"Alright! can you enter your {self.device} 7-digit Serial ID?")
                        computer_id = input(f"My {self.device}' ID is: ")
                        while(True):
                            if(len(computer_id) != 7 or computer_id.isdigit() == False):
                                laptop_id = input(f"Your {self.device} ID is invalid. Please re-enter a valid, 7 digit ID: ")
                            if(len(computer_id) == 7 and computer_id.isdigit() == True):
                                break 
                        print(f"Alright! Lets read your {self.device} data...")
                        time.sleep(2)
                        random_integer = random.randint(0, 6)
                        if(int(computer_id[random_integer]) > 5):
                            print("We are not recieving any signal from the address, from any sort of peripheal from your I/O. Please check connections.")
                        if(int(computer_id[random_integer]) <= 5):
                            print("It seems your IO drivers are outdated. Please try installing new drivers.")
            case "3":
                clear_terminal()
                print("Okay. Can you state your issue? \n 1: Battery life drains very fast \n 2: Overheats commonly")
                issue_phone = input("I am having issues with: \n ")
                match issue_phone:
                    case "1":
                        print("Alright! can you enter your username?")
                        phone_user = input("My user is: ")
                        while(True):
                            if(phone_user.isalpha() == False):
                                phone_user = input("Your username is invalid. Please re-enter a valid username: ")
                            if(phone_user.isalpha() == True):
                                break 
                        print(f"Alright! Lets read your {self.device} data...")
                        time.sleep(2)
                        random_integer = random.randint(0, 10)
                        random_integer2 = random.randint(14, 48)
                        if(int(random_integer) > 5):
                            print(f"It seems that your battery health is very low, being around {random_integer2}%. We reccomend getting your {self.device} checked out.")
                        if(int(random_integer) <= 5):
                            print(f"The abdundance of unused apps and excessive storage seem to be draining battery, as some upon boot up act as background applications. \nWe reccomend checking for unused apps and freeing up storage.")
                    case "2":
                        print("Alright! can you enter your username?")
                        phone_user = input("My user is: ")
                        while(True):
                            if(phone_user.isalpha() == False):
                                phone_user = input("Your username is invalid. Please re-enter a valid username: ")
                            if(phone_user.isalpha() == True):
                                break 
                        print(f"Alright! Lets read your {self.device} data...")
                        time.sleep(2)
                        random_integer = random.randint(0, 10)
                        if(int(random_integer) > 5):
                            print(f"Your {self.device} seems to be running many applications and processes at once. \nPlease try unloading apps that arent being, or not leaving the phone on for extended amounts of time with resource-heavy applications.")
                        if(int(random_integer) <= 5):
                            print("It seems that there may be some underlying internal issues. No applications seem to be using too many resources.")
                        





                
                        


                            
                        

                        





     

on = True
while on:
    print("Welcome! What is your name?")
    name1 = input()
    print("Now, what is your device?")
    device1 = input()
    user1 = User(name1, device1)
    user1.options()

            