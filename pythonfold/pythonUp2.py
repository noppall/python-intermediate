#static and class method
class person(object):
    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name," is ", self.age, " years old")


#staticmethod dan classmethod digunakan agar kita tidak membuat object baru
#classmethod tdk mengerti tentang self tetapi mengerti tentang instance pada class
#staticmethod membutuhkan argumen tapi bukan self

newPerson = person("nopal", 17)
#classmethod bisa dipanggil oleh semua instance di dalam class
print(person.getPopulation())
#staticmethod digunakan ketika kita tidak membutuhkan self dan tidak menggunakan actual object
print(person.isAdult(17)) 