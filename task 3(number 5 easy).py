class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        return "Звук животного"
    
    def __str__(self):
        return f"{self.name}, {self.age} лет"

class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"
    
    def fetch(self):
        return f"{self.name} приносит палку"

class Cat(Animal):
    def make_sound(self):
        return "Мяу-мяу!"
    
    def climb_tree(self):
        return f"{self.name} лазает по дереву"

if __name__ == "__main__":
    dog = Dog("Бобик", 3)
    cat = Cat("Мурка", 2)
    
    print(dog)
    print(dog.make_sound())
    print(dog.fetch())
    
    print(cat)
    print(cat.make_sound())
    print(cat.climb_tree())
