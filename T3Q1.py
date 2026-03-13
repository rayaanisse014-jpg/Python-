text = input('Enter a word or phrase: ')
vowels = ("a", "e", "i", "o", "u")
vowel_count = 0
consonant_count = 0
non_letter_count = 0
for char in text:
    if char.isalpha() and char.lower() in vowels:
      vowel_count += 1
    elif char.isalpha():
        consonant_count += 1 
    else:
        non_letter_count += 1
print(f'You entered: {text}')
print(f'Number of vowels: {vowel_count}')
print(f'Number of consonants: {consonant_count}')
print(f'Number of non-letter characters: {non_letter_count}')

if vowel_count > consonant_count:
    print('There are more vowels than consonants.')
elif consonant_count > vowel_count:
    print('There are more consonants than vowels.')
else:
    print('There are the same number of vowels and consonants.')
    
    