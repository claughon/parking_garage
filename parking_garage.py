from multiprocessing.resource_sharer import stop


class Parking:
    
    def __init__(self, tickets, parking_spaces):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        self.current_ticket = {}
        self.take_ticket()


    def take_ticket(self):
        while True:
            welcome = input("Do you want to park in the garage or are you leaving? (park/leave/quit)")
            if welcome.lower() == 'quit':
                break

            elif welcome.lower() == 'park':
                self.pay_for_parking()
                

            else: 
                welcome.lower() == 'leave'
                self.leave_garage()
                break
 
            


    # def p(self):
    #     print(self.tickets)
    #     print(self.parking_spaces)
    #     print(self.current_ticket)


    def pay_for_parking(self):
        # while True:
            if self.tickets == 0:
                print("There are no spaces in this garage, go elsewhere! \nThe passcode to get out is 123")
                # break
                self.take_ticket()
            else:
                hours = int(input("How many hours did you park with us? "))
                if hours <= 1:
                    self.current_ticket[self.tickets] = True
                    print(f"Your ticket # is {self.tickets}.")
                    self.tickets -= 1
                    self.parking_spaces -= 1
                    print(f"There are {self.parking_spaces} parking spaces left.")
                    print(f"Ticket costs $6. You have {hours} hrs to leave.")
                    self.take_ticket()

                elif hours <= 2:
                    self.current_ticket[self.tickets] = True
                    self.tickets -= 1
                    self.parking_spaces -= 1
                    print(f"Ticket costs $8. You have {hours} hrs to leave. Your ticket # is {self.tickets}")
                    self.leave_garage

                elif hours <= 4:
                    self.current_ticket[self.tickets] = True
                    self.tickets -= 1
                    self.parking_spaces -= 1
                    print(f"Ticket costs $10. You have {hours} hrs to leave. Your ticket # is {self.tickets}")
                    self.leave_garage

                elif hours <= 12:
                    self.current_ticket[self.tickets] = True
                    self.tickets -= 1
                    self.parking_spaces -= 1
                    print(f"Ticket costs $16. You have {hours} hrs to leave. Your ticket # is {self.tickets}")
                    self.leave_garage
                    
                elif hours <= 24:
                    self.current_ticket[self.tickets] = True
                    self.tickets -= 1
                    self.parking_spaces -= 1
                    print(f"Ticket costs $20. You have {hours} hrs to leave. Your ticket # is {self.tickets}")
                    self.leave_garage

                else:
                    self.current_ticket[self.tickets] = False
                    print("Ticket has not been paid. Enter how many hrs you want to park for...")
                    self.pay_for_parking
                    self.leave_garage()
        
        
    def leave_garage(self):
        leave = int(input("What is your ticket #? if no ticket enter passcode: "))
        
        if leave in self.current_ticket:
            if self.current_ticket[leave] == True:
                self.tickets += 1
                self.parking_spaces += 1
                print("Thank you have a nice day!")
                self.take_ticket()

        elif leave == 123:
            print("Sorry you couldn't park here, come another day!")

        else:
            print("Looks like you still need to pay! >:(")
            self.pay_for_parking()
            return


Garage = Parking(10,10)

