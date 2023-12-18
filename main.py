class Animal:
    def __init__(self, name):
        self.name = name
        
    def feed(self):
        pass
    
    def say(self):
        pass

class Cat(Animal):
    def feed(self):
        self.say()
        
    def say(self):
        print("喵喵，我是" + self.name)

class Dog(Animal):
    def feed(self):
        self.say()
        
    def say(self):
        print("汪汪，我是" + self.name)

class Person:
    def own(self, animal):
        if isinstance(animal, Animal):
            animal.feed()


# 生成实例并调用方法
cat = Cat("布丁")
dog = Dog("旺财")
person = Person()
person.own(cat)
person.own(dog)