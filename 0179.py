class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []
        self.grades = {}

    def enroll_course(self, course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)
            return f"Enrolled in {course_name}"
        return f"Already enrolled in {course_name}"

    def add_grade(self, course_name, grade):
        if course_name in self.courses:
            self.grades[course_name] = grade
            return f"Grade {grade} added for {course_name}"
        return f"Not enrolled in {course_name}"

    def calculate_gpa(self):
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

    def get_transcript(self):
        return f"Student: {self.name}, GPA: {self.calculate_gpa():.2f}"

# Create student object
student = Student("Alice", "S12345")

# 1. Test course enrollment
print(" === Course Enrollment Test ===")
print(student.enroll_course("Math"))
print(student.enroll_course("Science"))
print(student.enroll_course("Mash"))

# 2. Test adding grades
print("\n=== Grade Addition Test ===")
print(student.add_grade("Math", 90))
print(student.add_grade("Science", 85))
print(student.add_grade("History", 80))

# 3. Test GPA calculation
print("\n=== GPA Calculation Test ===")
print(f"Current GPA: {student.calculate_gpa():.2f}")

# 4. Tese transcript
print("\n=== Transcript Test ===")
print(student.get_transcript())

# 5. View student details
print("\n=== Student Details ===")
print(f"Name: {student.name}")
print(f"Student ID: {student.student_id}")
print(f"Enrolled Courses: {student.courses}")
print(f"Grade Records: {student.grades}")
