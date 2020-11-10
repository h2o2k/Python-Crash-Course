from collections import OrderedDict

favourite_languages = OrderedDict()

favourite_languages['john'] = 'python'
favourite_languages['paul'] = 'C'
favourite_languages['sarah'] = 'ruby'
favourite_languages['dayle'] = 'manga'

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " + language.title() + "!")
