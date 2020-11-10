for value in range(1, 6):  # printing values between 1 and 5
    print(value)

numbers = list(range(1, 6))  # using the list function to create a list of numbers
print(numbers)

evenNumbers = list(range(2, 11, 2))  # even numbers between 1 and 10
print(evenNumbers)


squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# this is a more efficient way of generating a list
newSquares = [value**2 for value in range(1, 11)]
print(newSquares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

players = ['sam', 'charles', 'paul', 'edgars']
print(players[0:3])  # slicing a list to get the values we want

# using a for loop in a list to get a certain amount of values
print("Here are the first 3 players on my team")
for player in players[:3]:
    print(player.title())

# copying lists and then adding new stuff into them
my_foods = ['pizza', 'banana', 'rice', 'chicken']
friend_foods = my_foods[:]
my_foods.append('dogfood')
friend_foods.append('polish apple juice')
print("My favourite foods are:")
print(my_foods)
print("My friends favourite foods are:")
print(friend_foods)

# This is now the start of the tuples
dimensions = (200, 50)
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nNew dimensions:")
for dimension in dimensions:
    print(dimension)
