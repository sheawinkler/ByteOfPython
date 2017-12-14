class Person:
    def __init__(self, name):
        self.name = name


    def say_hi(self):
        print('Hello, my name is', self.name)

    
p = Person('Shea')
p.say_hi()

    #or Person('Shea').say_hi()
