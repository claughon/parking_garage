from multiprocessing.resource_sharer import stop


class Parking:
    
    def __init__(self, tickets, parking_spaces):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = {}
       
 

    def pay_for_parking(self):
        if self.tickets == 0:
            print("There are no spaces in this garage, go elsewhere! \nThe passcode to get out is 123")
            
        else:
            hours = int(input("How many hours did you park with us? "))
            if hours <= 1:
                self.current_ticket[self.tickets] = True
                print(f"Your ticket # is {self.tickets}.")
                self.tickets -= 1
                self.parking_spaces -= 1
                print(f"There are {self.parking_spaces} parking spaces left.")
                print(f"Ticket costs $6. You have 1 hrs to leave.")
                

            elif hours <= 2:
                self.current_ticket[self.tickets] = True
                print(f"Your ticket # is {self.tickets}.")
                self.tickets -= 1
                self.parking_spaces -= 1
                print(f"There are {self.parking_spaces} parking spaces left.")
                print(f"Ticket costs $8. You have 2 hrs to leave.")
                

            elif hours <= 4:
                self.current_ticket[self.tickets] = True
                print(f"Your ticket # is {self.tickets}.")
                self.tickets -= 1
                self.parking_spaces -= 1
                print(f"There are {self.parking_spaces} parking spaces left.")
                print(f"Ticket costs $10. You have 4 hrs to leave.")
                

            elif hours <= 12:
                self.current_ticket[self.tickets] = True
                print(f"Your ticket # is {self.tickets}.")
                self.tickets -= 1
                self.parking_spaces -= 1
                print(f"There are {self.parking_spaces} parking spaces left.")
                print(f"Ticket costs $16. You have 12 hrs to leave.")
                
            elif hours <= 24:
                self.current_ticket[self.tickets] = True
                print(f"Your ticket # is {self.tickets}.")
                self.tickets -= 1
                self.parking_spaces -= 1
                print(f"There are {self.parking_spaces} parking spaces left.")
                print(f"Ticket costs $20. You have 24 hrs to leave.")

            else:
                self.current_ticket[self.tickets] = False
                print("You can only park here for a max 24 hours.")
                print("Please, enter valid response.")
                self.pay_for_parking
        
        
    def leave_garage(self):
        leave = int(input("What is your ticket number? If no ticket enter passcode: "))
        
        if leave in self.current_ticket:
            if self.current_ticket[leave] == True:
                self.tickets += 1
                self.parking_spaces += 1
                print("Thank you have a nice day!")
                

        elif leave == 123:
            print("Sorry you couldn't park here, come another day!")

        else:
            print("Ticket or passcode not recognized, please try again ")
            self.leave_garage
            return


Garage = Parking(10,10)


def take_ticket():
        while True:
            response = input("Do you want to park in the garage or are you leaving? (park/leave/quit)")
            if response.lower().strip() == 'quit':
                break

            elif response.lower().strip() == 'park':
                Garage.pay_for_parking()
                    

            elif response.lower().strip() == 'leave':
                Garage.leave_garage()
                
            
            else:
                print("That is not a valid response! Please pick one from the list")


take_ticket()