favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
    }

print(type(favorite_languages))

for name, language in favorite_languages.items():
    print(f"\n{name}")
    print(f"{name.title()}'s favorite language is {language.title()}.")
    
