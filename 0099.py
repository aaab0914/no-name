# Store information about a person
person_into = {
    'first_name':'Emily',
    'last_name':'Johnson',
    'age':25,
    'city':'London'
    }

# Display all information
print("=== Person Details ===")
for key,value in person_into.items():
    print(f"{key.replace('_',' ').title()}:{value}")
