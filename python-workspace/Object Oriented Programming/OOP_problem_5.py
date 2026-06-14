from random import randint

class Train():

    def __init__(self, trainNO):
        self.trainNO = trainNO

    def bookticket(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNO} from {fro} to {to}")
    
    def getStatus(self):
        print(f"Train No : {self.trainNO} is running ")
    
    def ticketFair(self, fro, to):
        print(f"Ticket fair from {fro} to {to} is {randint(222, 5555)}")

t = Train(122)
t.bookticket("Quetta" , "Peshawar")
t.getStatus()
t.ticketFair("Quetta", "Peshawar")
