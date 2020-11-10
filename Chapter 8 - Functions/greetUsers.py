def greetUsers(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'sarah', 'margot']
greetUsers(usernames)
