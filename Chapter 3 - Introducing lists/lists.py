bicycles = ['trek', 'mountain', 'speed', 'agility']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

message = "My first bicycle was a " + bicycles[2] + " bike."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')  # append adds to the end of the list
motorcycles.insert(0, 'BMW')  # inserts at a certain position in the list
print(motorcycles)

del motorcycles[0]  # deleting a certain index
print(motorcycles)

# "popping" an index which removes it and stores it in a variable
popped_motorcycle = motorcycles.pop(2)
print(motorcycles)
print("The last motorcycle I owned was a " + popped_motorcycle)

tooExpensive = 'honda'
# deleting a value without knowing the index, may need to use a loop if the value appears more than once
motorcycles.remove(tooExpensive)
print(motorcycles)
print("\nA " + tooExpensive.title() + " is too much for me.\n")

cars = ['bmw', 'audi', 'renault', 'peugeot']
# cars.sort() # this is a permanent way of changing a list
# cars.sort(reverse=True) # Z-A as opposed to A-Z
# cars.reverse() # reverses the list permanent
# sorted function is a temp way of changing the list and can be reversed as well
print(sorted(cars, reverse=True))
print(cars)

print(len(cars))  # len can get the length of a list
