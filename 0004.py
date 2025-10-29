requested_toppings=['mushrooms','green pappers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping=='green pappers':
        print("Sorry, we are not of green pappers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")
