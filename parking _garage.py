#Parking _Garage

class ParkingGarage():
    currentTicket = {}
    tickets = ["1", "2", "3", "4"] # , 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    parkingSpaces = ["1", "2", "3", "4"]# , 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    """
    Attributes info:
        "currentTicket" is a dictionary. It should be empty upon initialization.
        "tickets" is a list. It updates as people come in and leave.
        "parkingSpaces" is a list. It updates as people come in and leave.
    """
    
    def payParking(self, ticket_num):       
        if self.currentTicket.get(ticket_num) == True:
            print("Thank you, but you've already paid! You have 15 minutes to leave")
        else:
            amount = input("The parking rate is $15.00. How much are you paying ?  ")
            while True:
                if amount == "$15.00" or amount == "$15" or amount == "15" or amount == "15.00" :
                    print("Paid! You have 15 minutes to leave")                
                    self.currentTicket[ticket_num] = True
                    break
                else: 
                    print("Please pay the amount of $15.00")
                    amount = input("The parking rate is $15.00. How much are you paying ?  ")


    def takeTicket(self):
        if self.parkingSpaces == []:
            print("Sorry, we don't have space left.")
        else:
            print("Here is your ticket!")
            key_ind = self.tickets.pop()
            self.parkingSpaces.pop()
            self.currentTicket[key_ind] = False
            print(f"Your ticket number is {key_ind}. Don't forget it!")

    
    def leaveGarage(self):
        ticket_num = input("Please enter your ticket number: ")
        self.ticketCheck(ticket_num)
        self.payParking(ticket_num) 
        self.tickets.append(ticket_num)
        self.parkingSpaces.append(ticket_num)
        print("Thank you, have a nice day!")


    def seeGarage(self):
        if len(self.parkingSpaces) > 0:
            print(f"Currently, we have space for {str(len(self.parkingSpaces))} more cars.")
        else:
            print("It looks like we're full!")

    def ticketCheck(self,ticket_num):
        while True:
            if ticket_num in self.currentTicket.keys(): 
                break 
            else:
                print(" We can't find that ticket number")
                ticket_num = input("Please enter your ticket number: ")







new_york_garage = ParkingGarage()

def go__to_garage():
#    try:
    print("Welcome to the New York Garage!")
    action = input("What would you like to do?\n Park / See Space / Pre-Pay / Leave: ")
    while True:
        if action.lower() == "park":
            new_york_garage.takeTicket()
            action = input("What would you like to do?\n Park / See Space / Pre-Pay / Leave: ")
        elif action.lower() == "see space" or action.lower() == "see" or action.lower() == "space":
            new_york_garage.seeGarage()
            action = input("What would you like to do?\n Park / See Space / Pre-Pay / Leave: ")
        elif action.lower() == "pay" or action.lower() == "pre-pay" or action.lower() == "prepay" or action.lower() == "pre pay":
            if new_york_garage.currentTicket == {}:
                print("\nSorry, you must park first.")
                action = input("What would you like to do?\n Park / See Space / Pre-Pay / Leave: ")
            else:
                ticket_num = input("\nPlease enter your ticket number: ")
                new_york_garage.ticketCheck(ticket_num)
                new_york_garage.payParking(ticket_num)
                action = input("What would you like to do?\n Park / See Space / Pre-Pay / Leave: ")
        elif action.lower() == "leave":             
            if new_york_garage.currentTicket == {}:
                print("\nSorry, you must park first.")
                action = input("What would you like to do?\n Park / See Space / Pre-Pay / Leave: ")
            else:
                new_york_garage.leaveGarage()
                break
        else:
            print("\nSorry, try again!")
            action = input("What would you like to do?\n Park / See Space / Pre-Pay / Leave: ")
#    except:
#       print("\nSorry, we seem to have run into an error. Please visit another time!")

go__to_garage()