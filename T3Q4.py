PROMPT = 'Enter a word (or QUIT to finish): '
words = []
word = input(PROMPT)
while word != 'QUIT':
    words.append(word)
    word = input(PROMPT)
print(f'The words are: {words}')
if len(words) == 0:
    print('There were no words entered.')
else:
    first_words = words[0]
    all_same = True
    
    for w in words:
        if w != first_words:
            all_same = False
            break
    if all_same:
        print('All the words are the same.')
    else:
        print('The words are not all the same.')
    