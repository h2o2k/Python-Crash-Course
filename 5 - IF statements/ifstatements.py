cars = ['audi', 'bmw', 'honda', 'renault']
for car in cars:
    if car == 'bmw':  # equal to
        print(car.upper())
    else:
        print(car.title())

answer = 24
if answer != 42:
    print("\nThat is not the correct number\n")

age = 20
if age >= 18:
    print("\nYou old")
else:
    print("\nBack to school")

amusementAge = 121
if amusementAge < 4:
    print("\nYou get in free")
elif amusementAge < 18:
    print("\n5 bucks")
elif amusementAge < 65:
    print("\n50 bucks")
elif amusementAge >= 65:
    print("\nFree")

requestedToppings = ['cheese', "mushrooms"]  # using individual if statements
if 'mushrooms' in requestedToppings:  # to ensure that they all are checked
    print("\nAdding mushrooms")
if 'pineapple' in requestedToppings:
    print("\nAdding pineapple")
if 'cheese' in requestedToppings:
    print("\nAdding cheese")
print("\nAlright pimp your pizza is done\n")

requested_toppings = ['cheese',  'peppers', 'mushrooms', ]
for requested_topping in requested_toppings:
    if requested_topping == 'peppers':
        print("Sorry we are outta peppers right now")
    else:
        print("Adding " + requested_topping + ".")
print("PIZZA READY")
