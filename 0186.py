class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}")

    def promote(self):
        self.grade += 1
        print(f"{self.name} promoted to grade {self.grade}")

student1 = Student("John Smith", 15, 9)
student1.display_info()
student1.promote()
