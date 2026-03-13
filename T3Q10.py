PROMPT = input('Enter words separated by spaces: ')
line = PROMPT.split(" ")
WORD_LIST = []
for piece in line:
    piece = piece.strip()
    if piece != "":
        WORD_LIST.append(piece)
print(f'The words are: {WORD_LIST}')
if len(WORD_LIST) == 0:
    print('There are no words.')
else:
    sorted_word = sorted(WORD_LIST)
    words_differ = True
    for i in range(1, len(sorted_word)):
        if sorted_word[i] == sorted_word[i - 1]:
          words_differ = False
          break
    if words_differ:
        print('All words are different.')
    else:
        print('Not all words are different.')

