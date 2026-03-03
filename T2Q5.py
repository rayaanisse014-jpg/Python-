one_character = input('Enter one character: ')

if one_character.isalpha():
    if one_character.lower() in "a,e,i,o,u":
        print('That character is a vowel.')
    else:
        print('That character is a consonant.')
else:
        print('That character is not a letter.')