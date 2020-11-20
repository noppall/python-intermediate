class Pet:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old and I'm {self.color}")

class Cat(Pet):
    def __init__(self, name, age, color, typee):
        Pet.__init__(self, name, age, color)
        self.typee = typee
        print(f"I am a {self.typee}")

    def meow(self):
        print("Meow")

class Dog(Pet):
    def bark(self):
        print("Guk")


roy = Cat("Roy", 100, "brown", "kucing") 
roy.show()
rega = Dog("Rega", 10, "pink")
rega.show()

#super berguna untuk memanggil init class parent