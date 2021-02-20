class Train():
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = [1, 2, 3, 4, 5, 6, 7, 8 ,9 ,10]

    def getStatus(self):
        print(
            f"The name of the train is {self.name}, it has {len(self.seats)} seats left")

    def fareInfo(self):
        print(f"The Fare of the train is {self.fare}")

    def bookTickets(self, seatNo):
        if(len(self.seats) > 0):
            print("Your Seat has been booked")
            self.seats.remove(seatNo)
        else:
            print("We are sorry but the train is full")
    
    def cancelTicket(self, seatNo):
        print("Your ticket has been cancelled")
        self.seats = self.seats.append(seatNo)
# Intercity train details:
intercity1 = Train("GhaziabadEXP", 190, 300)
intercity2 = Train("NoidaEXP", 100, 500)
# National train details:
nt1 = Train("Rajdhani", 1000, 900)
nt2 = Train("Shatabdi", 2000, 1000)

ans = input("Do you want to book intercity trains(IN) or National Trains(NT) ")
if ans == "IN":
    intercity1.getStatus()
    intercity2.getStatus()
    fare = int(input(
        f"Do you want to know the fares of these trains?\n To know the fare for {intercity1.name} Train Press 1 and To Know the fare of {intercity2.name} train press 2: "))
    seatNo = int(input("Enter the seat no. you want: "))
    if  fare == 1:
        intercity1.fareInfo()
        tic = input("Do you want to book a ticket?\n 'Y' or 'N' ")
        if tic == "Y":
            intercity1.bookTickets(seatNo)
            can = input("If you want to cancel your ticket type C if you don't want to cancel type N: ")
            if can == "C":
                intercity1.cancelTicket(seatNo)
            else:
                print("Okay then it is booked")
    elif fare == 2:
        intercity2.fareInfo()
        tic = input("Do you want to book a ticket?\n 'Y' or 'N' ")
        if tic == "Y":
            intercity2.bookTickets(seatNo)
            can = input("If you want to cancel your ticket type C if you don't want to cancel type N: ")
            if can == "C":
                intercity2.cancelTicket(seatNo)
            else:
                print("Okay then it is booked")
    else:
        print("Pls choose between the above options only")

elif ans == "NT":
    nt1.getStatus()
    nt2.getStatus()
    fare =int(input(
        f"Do you want to know the fares of these trains?\n To know the fare for { nt1.name} Train Press 1 and To Know the fare of {nt2.name} train press 2: "))
    seatNo = int(input("Enter the seat no. you want: "))
    if fare == 1:
        nt1.fareInfo()
        tic = input("Do you want to book a ticket?\n 'Y' or 'N':  ")
        if tic == "Y":
            nt1.bookTickets(seatNo)
            can = input("If you want to cancel your ticket type C if you don't want to cancel type N: ")
            if can == "C":
                intercity2.cancelTicket(seatNo)
            else:
                print("Okay then it is booked")
    elif fare == 2:
        nt2.fareInfo()
        tic = input("Do you want to book a ticket?\n 'Y' or 'N' ")
        if tic == "Y":
            nt2.bookTickets(seatNo)
            can = input("If you want to cancel your ticket type C if you don't want to cancel type N: ")
            if can == "C":
                intercity2.cancelTicket(seatNo)
            else:
                print("Okay then it is booked")
    else:
        print("Pls choose between the above options only")
    

else:
    print("Pls type a Right Option")