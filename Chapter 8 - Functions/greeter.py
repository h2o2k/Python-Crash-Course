def getFormattedName(firstName, lastName):
    fullName = firstName + ' ' + lastName
    return fullName.title()

while True:
    print('\nWhat is your name? ')
    print("(Enter 'q' at any time to quit)")

    fName = input("First name: ")
    if fName == 'q':
        break

    lName = input("Last name: ")
    if lName == 'q':
        break

    formattedName = getFormattedName(fName, lName)
    print("\nHello, " + formattedName + "!")
