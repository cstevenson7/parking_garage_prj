#Parking _Garage

class ParkingGarage():
    customer_dict = {}
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    spaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#     def __init__(self,tickets,spaces):
#        self.tickets = tickets
#        self.spaces = spaces
    
    def payParking(self):
        print("Paid!")
        # ACTUALLY DO SOMETHING HERE


    def takeTicket(self):
        print("Here is your ticket!")
        key_ind = self.tickets.pop(0)
        self.customer_dict[key_ind] = False
        print(f"Your ticket number is {key_ind}. Don't forget it!")
        pay_option = input("Would you like to pay now? Y/N: ")
        if pay_option.lower() == "y":
            self.payParking()
        elif pay_option.lower() == "n":
            print("Enjoy your stay!")
        else:
            print("I'm sorry, that's not an option. Try again!")
            pay_option = input("Would you like to pay now? Y/N: ")



new_york_garage = ParkingGarage()

def go__to_garage():
    print("Welcome to the New York Garage!")
    action = input("What would you like to do?\n Park / See Space / Leave: ")
    while True:
        if action.lower() == "park":
            new_york_garage.takeTicket()
            action = input("What would you like to do?\n Park / See Space / Leave: ")
#        elif action.lower() == "see space" or action.lower() == "see" or action.lower() == "space":
#            new_york_garage.seeSpace()
#            action = input("What would you like to do?\n Park / See Space / Leave: ")
        elif action.lower() == "leave":
#            new_york_garage.leaveGarage()
            break
        else:
            print("Sorry, try again!")
            action = input("What would you like to do?\n Park / See Space / Leave: ")

go__to_garage()