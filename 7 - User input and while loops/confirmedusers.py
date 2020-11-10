unconfirmedUsers = ['alice', 'brian', 'candace']
confirmedUsers = []

while unconfirmedUsers:
    currentUser = unconfirmedUsers.pop()
    print("Verifying user: " + currentUser.title())
    confirmedUsers.append(currentUser)

for confirmedUser in confirmedUsers:
    print(confirmedUser.title())
