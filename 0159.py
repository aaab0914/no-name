def calculate_grade(score):
    """ Calculate grade based on score """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"
    
print("=== Student Grades ===")
grade1 = calculate_grade(85)
print(f"Student 1 grade: {grade1}")

grade2 = calculate_grade(92)
print(f"Student 2 grade: {grade2}")

grade3 = calculate_grade(68)
print(f"Student 3 grade: {grade3}")
