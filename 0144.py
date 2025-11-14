# Exercise 7-4: Pizza Toppings
print("=== Exercise 7-4: Pizza Toppings ===")

prompt = "\nPlease enter a pizza topping (enter 'quit' to finish):"

while True:
	topping = input(prompt)
	
	if topping == 'quit':
		break
	else:
		print(f"I'll add {topping} to your pizza!")
