# Exercise 7-5: Movie Tickets
print("\n=== Exercise 7-5: Movie Tickets ===")

while True:
	age = input("\nPlease enter your age (enter 'quit' to exit):")
	
	if age == 'quit':
		break
		
	age = int(age)
	
	if age < 3:
		print("Your ticket is free!")
	elif age <= 12:
		print("Your ticket cost $10.")
	else:
		print("Your ticket costs $15.")
		
