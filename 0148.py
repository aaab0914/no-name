# 6-5. Rivers: Make a dictionary containing three major rivers
rivers = {
    'nile':'egypt',
    'amazon':'bazhil',
    'yangtze':'china',
    'mississippi':'united states',
    'danube':'germany'
    }

print("=== Exercise 6-5: Rivers ===")

#	Use a loop to print a sentence about each river
print("\n1. Sentence about each river:")
for river, country in rivers.items():
	print(f"The {river.title()} runs through {country.title()}.")

#	Use a loop to print the name of each river included in the dictionary
print("\n2. Name of all rivers:")
for river in rivers.keys():
	print(f"- {river.title()}")
	
#	Use a loop to print the name of each country included in the dictionary
print("\n3. Names of all country:")
for country in rivers.values():
	print(f"- {country.title()}")
	
