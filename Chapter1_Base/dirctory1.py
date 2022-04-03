if __name__ == '__main__':
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }
    for name, language in favorite_languages.items():
        print(name.title() + "'s favourite language is " +
              language.title() + '.')
    # traverse all the keys
    for name in favorite_languages.keys():
        print(name.title())
    # traverse all the values
    for value in favorite_languages.values():
        print(value.title())

    print('The following languages have been mentioned:')
    all_language = set(favorite_languages.values())
    for i in all_language:
        print(i)
        
