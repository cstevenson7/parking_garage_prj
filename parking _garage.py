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
    
    def payParking(self, ticket_num, action = ""):       
        if self.currentTicket.get(ticket_num) == True:
            print("\nThank you, you've already paid! You have 15 minutes to leave")
        else:
            amount = input("\nThe parking rate is $15.00. How much are you paying ?  ")
            while True:
                if amount == "$15.00" or amount == "$15" or amount == "15" or amount == "15.00" :
                    if action == "prepay":
                        print("\nThank you for pre-paying!\n")
                        self.currentTicket[ticket_num] = True
                        break
                    else:
                        print("\nPaid! You have 15 minutes to leave\n")                
                        self.currentTicket[ticket_num] = True
                        break
                else: 
                    print("\nPlease pay the amount of $15.00")
                    amount = input("\nThe parking rate is $15.00. How much are you paying ?  ")
  

    def takeTicket(self):
        if self.parkingSpaces == []:
            print("\nSorry, we don't have space left.")
        else:
            print("\nHere is your ticket!")
            key_ind = self.tickets.pop()
            self.parkingSpaces.pop()
            self.currentTicket[key_ind] = False
            print(f"\nYour ticket number is {key_ind}. Don't forget it!\n")

    
    def leaveGarage(self):
        ticket_num = input("\nPlease enter your ticket number: ")
        self.ticketCheck(ticket_num)
        self.payParking(ticket_num) 
        self.tickets.append(ticket_num)
        self.parkingSpaces.append(ticket_num)
        print("\nThank you, have a nice day!\n")


    def seeGarage(self):
        if len(self.parkingSpaces) > 0:
            print(f"\nCurrently, we have space for {str(len(self.parkingSpaces))} more cars.\n")
        else:
            print("\nIt looks like we're full!")


    def ticketCheck(self,ticket_num):
        while True:
            if ticket_num in self.currentTicket.keys(): 
                break 
            else:
                print("\nWe can't find that ticket number")
                ticket_num = input("\nPlease enter your ticket number: ")



new_york_garage = ParkingGarage()

def go__to_garage():
#    try:
    print("Welcome to the New York Garage!\n")
    while True:
        action = input("\nWhat would you like to do?\n Park / See Space / Pre-Pay / Leave / Quit: ")
        if action.lower() == "park":
            new_york_garage.takeTicket()
        elif action.lower() == "see space" or action.lower() == "see" or action.lower() == "space":
            new_york_garage.seeGarage()
        elif action.lower() == "pay" or action.lower() == "pre-pay" or action.lower() == "prepay" or action.lower() == "pre pay":
            if new_york_garage.currentTicket == {}:
                print("\nSorry, you must park first.")               
            else:
                ticket_num = input("\nPlease enter your ticket number: ")
                new_york_garage.ticketCheck(ticket_num)
                action= "prepay"
                new_york_garage.payParking(ticket_num, action)               
        elif action.lower() == "leave":             
            if new_york_garage.currentTicket == {}:
                print("\nSorry, you must park first.\n")
            else:
                new_york_garage.leaveGarage()
        elif action.lower() == "quit":
            print("\nSee you next time.\n")
            break 
        else:
            print("\nSorry, try again!")            
#    except:
#       print("\nSorry, we seem to have run into an error. Please visit another time!")

go__to_garage()