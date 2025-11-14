def calculate_area(length, width):
    """ Calculate rectangle area """
    area = length * width
    return area

# Main program = multiple function calls
print("=== Area Calculation ===")
area1 = calculate_area(5, 3)
print(f"Rectangle 1 area: {area1}")

area2 = calculate_area(8, 4)
print(f"Rectangle 2 area: {area2}")

area3 = calculate_area(10, 6)
print(f"Rectangle 3 area: {area3}")