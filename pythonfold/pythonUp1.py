#parameter optional 
class car(object):
    def __init__(self, make, model, year, condition='used', kms=0):
        self.make = make
        self.model = model
        self.year = year
        self.condition =condition
        self.kms = kms

    def display(self, showAll):
        if showAll:
            print("This car is a %s %s from %s, it is %s and has %s kms" %(self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("This car is a %s %s from %s" %(self.make, self.model, self.year))


tumbas = car('toyota', 'supra', 1998, 'used', 10000)
tumbas.display(True)



def func(x=1, y=1):
    return x **2

print(func(2,2))

