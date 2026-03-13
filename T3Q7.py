PROMPT = input('Enter some words separated by spaces: ')
Split = PROMPT.split(" ")
words = []
for piece in Split:
    if piece != "":
        words.append(piece)
print(f'The words are: {words}')
if len(words) == 0:
    print('There are no words.')
elif len(words) == 1:
    print('There is one word.')
else:
    print(f'There are {len(words)} words.')
    