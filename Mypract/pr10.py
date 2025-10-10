#class Person:

    #def _init_(self, name, age):
        #self.name = name  # имя человека
        #self.age = age  # возраст человека

#tom = Person("Tom", 22)
#bob = Person("Bob", 43)

#print(tom.name)         # Tom
#print(bob.name)         # Bob

#class Student:
    #def __init__(self,  name, age):
        #self.name = name
        #self.age = age
#Adil = Student("Adil",  "18")
#Rasul = Student("Rasul", 16)
#print("Имя студента:", Adil.name)
#print("Сколько лет:", Adil.age)
#print("Имя Студента", Rasul.name)
#print("Сколько лет", Rasul.age)

class Car:
    def __init__(self, name, colour, wheels):
        self.name = name
        self.colour = colour
        self.wheels = wheels
        self.speed = 0

    def car_info(self):
        print(f"Машина: {self.name}, цвет: {self.colour}, Колеса: {self.wheels}, скорость: {self.speed} км/ч")
    def drive(self, speed):
        self.speed = 0
        print(f"{self.name} едет со скоростью {self.speed} км/ч")
    def stop(self):
        self.speed = 0
        print(f"{self.name} остановилась")

toyota = Car(name= "toyota", colour= "white", wheels= "summer")

toyota.car_info()
toyota.car.drive(80)
toyota.car.stop()





