class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    def get_student_detail(self):
        print("Age : ", self.age)
        print("Marks : ", self.marks)

    def assign_course(self, name):
        self.name = name
        c = []
        


s1 = Student("Mars", 19, 89)
s2 = Student("Hello", 18, 78)

s2.get_student_detail()


