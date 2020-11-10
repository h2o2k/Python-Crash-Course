alien_0 = {'color': 'green', 'points': '5', 'speed': 'slow'}
print(alien_0)
alien_0['x_pos'] = 0
alien_0['y_pos'] = 25
print(alien_0)
alien_0['color'] = 'red'
print("The alien is now the color " + alien_0['color'])
del alien_0['points']
print(alien_0)

favouriteLanguages = {'john': 'python',
                      'paul': 'c',
                      'conor': 'japanese'}
print("John's favourite programming language is " + favouriteLanguages['john'].title())
for key, value in favouriteLanguages.items():
    print('\nName: ' + key)
    print('Language: ' + value)
for name in sorted(favouriteLanguages.keys()):  # grabbing only the key values
    print(name.title())
for language in favouriteLanguages.values():  # grabbing only the values
    print(language.title())

alien_1 = {'color': 'red', 'points': '5'}
alien_2 = {'color': 'yellow', 'points': '10'}
alien_3 = {'color': 'green', 'points': '15'}
aliens = [alien_1, alien_2, alien_3]
for alien in aliens:
    print(alien)
