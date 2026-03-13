PROMPT = input('Enter integers separated by commas: ')
Split = PROMPT.split(",")
numbers = []
for piece in Split:
    piece = piece.strip()  # remove spaces
    if piece  != "":
        numbers.append(int(piece))
print(f'The numbers are: {numbers}')

if len(numbers) == 0:
    print('The median is not defined for an empty list.')
else:
    sorted_numbers = sorted(numbers)
    midpoint = len(sorted_numbers) // 2    
    print(f'The sorted numbers are: {sorted_numbers}')
    if len(numbers) % 2 == 1:   # odd length
        median = sorted_numbers[midpoint] 
    else:
        median  = (sorted_numbers[midpoint - 1] + sorted_numbers[midpoint]) / 2
    print(f'The median is {median}.')
    

    