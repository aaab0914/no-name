print("What kind of car you like?")
available_to_rent_list1 = ('C 300','RAV4','3 Series','Camry','X3')
print(f"We have {available_to_rent_list1}.")

car_names = input("I want:")

if car_names in available_to_rent_list1:
    print(f"Let me see if I Can find you a {car_names}.")
else:
    print(f"Sorry, we don't have {car_names} available.")
