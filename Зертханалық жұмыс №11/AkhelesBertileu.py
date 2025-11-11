import math

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}")

student = Student("Aigerim", 21, "ST1023")
student.display_info()

class Vehicle:
    def fuel_efficiency(self):
        pass

class Car(Vehicle):
    def __init__(self, distance, fuel_used):
        self.distance = distance
        self.fuel_used = fuel_used

    def fuel_efficiency(self):
        return self.distance / self.fuel_used

class ElectricScooter(Vehicle):
    def __init__(self, distance, battery_used):
        self.distance = distance
        self.battery_used = battery_used

    def fuel_efficiency(self):
        return self.distance / self.battery_used

vehicles = [Car(450, 30), ElectricScooter(60, 15)]

for v in vehicles:
    print(f"Efficiency: {v.fuel_efficiency():.2f}")

class Animal:
    def speak(self):
        print("This animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("The dog barks: Woof! Woof!")

class Cat(Animal):
    def speak(self):
        print("The cat meows: Meow! Meow!")

a = Animal()
d = Dog()
c = Cat()

a.speak()
d.speak()
c.speak()

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6)]

for shape in shapes:
    print("Area:", shape.area())

class Warrior:
    def ability(self):
        print("Fighting with a sword ⚔️")

class Wizard:
    def ability(self):
        print("Casting magical spells ✨")

class Battlemage(Warrior, Wizard):
    def ability(self):
        super().ability()
        print("Also channeling arcane energy 🔮")

hero = Battlemage()
hero.ability()

class Teacher:
    def role(self):
        print("Teaching students.")

class Researcher:
    def role(self):
        print("Conducting research.")

class Professor(Teacher, Researcher):
    def role(self):
        super().role()
        print("Also managing academic projects.")

p = Professor()
p.role()
