import random

class Human:
    def __init__(self,name="Human",job=None,home=None,car=None,love = 50):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car
        self.love = love

    def get_home(self):
        self.home = House()


    def get_car(self):
        self.car = Auto(brand)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(jobs)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")

        else:
            if self.satiety >= 100:
                self.satiety =10
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4


    def shopping(self,manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("Ми придбали пальне")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Ми купили їжу")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Ура смакота!!!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15


    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strenght += 100
        self.money -= 50


    def day_stat(self, day):
        print(f"Сьогодні {day} з життя {self.name}")
        print(f"{day:=^50}","\n")

        human_indexes = self.name + " парамерти"
        print(f"{human_indexes:^40}","\n")
        print(f"Ситість : {self.satiety}")
        print(f"Гроші : {self.money}")
        print(f"Щастя : {self.gladness}")
        home_indexes = "Параметри будинка"
        print(f"{home_indexes:^40}", "\n")
        print(f"Безлад {self.home.mess}")
        print(f"Їжа: {self.home.food}")
        car_indexes = f"Параметри {self.car.brand}"
        print(f"{car_indexes:^40}", "\n")
        print(f"Пальне: {self.car.fuel}")
        print(f"Двигун: {self.car.strenght}")


    def is_alive(self):
        if self.gladness <0:
            print("Сумно аж за край:/")
            return False
        if self.satiety <0:
            print("Капєц:(")
            return False
        if self.money <= 200:
            print("Банкрот....:(")
            return False


    def live(self,day):
        if self.is_alive():
            return False
        if self.home is None:
            print("Періїзджаємо!!!")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"Я купив собі {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"Я влаштувався працювати {self.job.job},"
                  f"моя зарплата {self.job.salary}")

        self.day_stat(day)



        dice = random.randint(1,4)
        if self.satiety <20:
            print("Іду їсти")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("В кімнаті безладб треба прибрати ....")
                self.clean_home()
            else:
                print("Ураа! Відпочинок!!!!")
                self.chill()
        elif self.money < 0:
            print("Йдемо на роботу....")
            self.work()
        elif self.car.strenght < 15:
            print("Треба поремонтувати авто...")
            self.to_repair()
        elif dice == 1:
            print("Ура!!Відпочинок!")
            self.chill()
        elif dice == 2:
            print("Йдемо на роботу...")
            self.work()
        elif dice == 3:
            print("В кімнаті безлад, треба прибрати")
            self.clean_home()


        elif dice == 4:
            print("Купуємо солодощі")
            self.shopping(manage="delicacies")
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0











class Auto:
    def __init__(self,brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strenght = brand_list[self.brand]["strenght"]
        self.consumption = brand_list[self.brand]["consumption"]


    def drive(self):
        if self.strenght > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strenght -= 1
            return True
        else:
            print("Машина не на ходу :(")
            return False


class Job :
    def __init__(self,jobs):
        self.job = random.choice(list(jobs))
        self.salary = jobs[self.job]["salary"]
        self.gladness_less = jobs[self.job]["gladness_less"]




brand = {
    "BMW":{"fuel":100, "strenght":100, "consumption":6},
    "Audi":{"fuel":110, "strenght":90, "consumption":8},
    "Mers":{"fuel":90, "strenght":135, "consumption":10},
    "Moskvich":{"fuel":75, "strenght":70, "consumption":4},
    "Volha":{"fuel":80, "strenght":130, "consumption":9}
}

jobs = {
    "Python Developer":{"salary" :2000,"gladness_less":11},
    "C# Decktop Developer":{"salary" :2100,"gladness_less":8},
    "Lawyer":{"salary" :3000,"gladness_less":9},
    "Mechanic":{"salary" :1500,"gladness_less":7},
    "Policeman":{"salary" :1700,"gladness_less":12}
}

human = Human(name="Marko")
for day in range(1,8):
    if human.live(day) == False:
        break