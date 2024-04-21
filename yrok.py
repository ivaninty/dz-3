class Human:
    def __init__(self, name = "noname"):
        self.name = name

class Auto:
    def __init__(self,brand):
        self.brand = brand
        self.passengers = []


    def add_passenger(self, *args):
        for  passenger in args:
           self.passengers.append(passenger)


    def print_passengers(self):
        if self.passengers != []:
            print(f"Імена пасажирів{self.brand}:")
            for passengers in self.passengers:
                print(passengers.name)
        else:
                print(f"У {self.brand} немає пасажирів")


pass1 = Human("Настя")
pass2 = Human("Григорій")
pass3 = Human("Вадим")

car1 = Auto("BMW")
car2 = Auto("Audi")

car1.add_passenger(pass1,pass2,pass3)
car2.add_passenger(pass1,pass3)

car1.print_passengers()
car2.print_passengers()