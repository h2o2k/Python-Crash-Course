def buildPerson(firstName, lastName,age=''):
    person = {'first': firstName, 'last': lastName}
    if age:
        person['age'] = age
    return person

musician = buildPerson('kendrick', 'lamar', age=21)
print(musician)
