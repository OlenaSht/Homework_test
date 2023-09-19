class Animals:
    def __init__(self, name, age, type1):
        self.name = name
        self.age = age
        self.type = type1

    def greetings(self):
        return f'Hi, {self.name}, we are adopting you!'

    def calculation(self):
        return f'Next year you will be {self.age + 1} year old'


animal1 = Animals('Rex', 5, 'husky')
animal2 = Animals(type1 = 'JackRusselTerrier', age = 2, name = 'Ted')
print(animal1.__dict__)
print(animal2.__dict__)
print(animal1.name)
print(animal2.greetings())
print(animal1.calculation())

class Doggos(Animals):
    def __init__(self, name, age, type1, fur_color, eye_color):
        super().__init__(name, age, type1)
        self.fur_color = fur_color
        self.eye_color = eye_color

    def confession(self):
        return 'I love doggos!'

dog1 = Doggos('Larry', 1, 'rotweiler', 'brown', 'blue')
dog2 = Doggos('Terry', 6, 'labrador', 'grey', 'brown')
print(dog2.__dict__)
print(dog2.calculation())
print(dog2.confession())
