class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def check_grade(self):
        if self.score >= 90:
            print(f"{self.name}: Excekkent! Grade A")
        elif self.score >= 80:
            print(f"{self.name}: Good! Grade B")
        elif self.score >= 70:
            print(f"{self.name}: Average! Grade C")
        elif self.score >= 60:
            print(f"{self.name}: Pass! Grade D")
        else:
            print(f"{self.name}: Fail Grade F")
            
# Test
student1 = Student("John", 85)
student2 = Student("Alice", 45)
student1.check_grade()
student2.check_grade()