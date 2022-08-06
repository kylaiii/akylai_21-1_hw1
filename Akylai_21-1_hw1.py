
class Dog:
    def __init__(self, name):
        self.name = name
    def voice(self):
        print(f'{self.name}: gaf gaf gaf')

togo = Dog('Togo')
togo.voice()

class Cow:
    def __init__(self, name):
        self.name = name
    def voice(self):
        print(f'{self.name}: moo moo moo')

cow = Cow('Cow')
cow.voice()

class Cat:
    def __init__(self, name):
        self.name = name
    def voice(self):
        print(f'{self.name}: meow meow')

kitty = Cat('Kitty')
kitty.voice()

class Bear:
    def __init__(self, name):
        self.name = name
    def voice(self):
        print(f'{self.name}: grrrr grrrr')

bear = Bear('Bear')
bear.voice()




