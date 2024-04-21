class Human:
    def __init__(self, name = "noname"):
        self.name = name

class Pole:
    def __init__(self,pol):
        self.pol = pol
        self.footboler = []


    def add_footboler(self, *args):
        for  foot in args:
           self.footboler.append(foot)


    def print_footboler(self):
        if self.footboler != []:
            print(f"Імена Футболістів{self.pol}:")
            for footboler in self.footboler:
                print(footboler.name)
        else:
                print(f"У {self.pol} немає пасажирів")


fot1 = Human("Настя")
fot2 = Human("Григорій")
fot3 = Human("Вадим")

pol1 = Pole(": на полі 1")


pol1.add_footboler(fot1,fot2,fot3)


pol1.print_footboler()
