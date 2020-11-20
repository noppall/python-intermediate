#oop yokk
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade =grade

    def get_grade(self):
        return self.grade
        
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student) 
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)        

siswa1 = Student("nopal", 17, 100)
siswa2 = Student("yugo", 17, 50)
siswa3 = Student("fina", 18, 100)
siswa4 = Student("robert", 20, 65)
siswa5 = Student("minke", 20, 99)

IPA = Course("science", 5)
IPA.add_student(siswa1)
IPA.add_student(siswa2)
IPA.add_student(siswa3)
IPA.add_student(siswa4)
IPA.add_student(siswa5)

print(IPA.students[0].name)
print(IPA.get_average_grade())
print(len(IPA.students))

