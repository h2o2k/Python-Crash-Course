responses = {}

pollingActive = True

while pollingActive:
    name = input("\nWhats your name? ")
    response = input("And which mountain would you like to climb? ")

    responses[name] = response

    repeat = input("Would you like anyone else to take this poll? (yes/no) ")
    if repeat == 'no':
        pollingActive = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response)
