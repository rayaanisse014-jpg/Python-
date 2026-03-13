count = int(input('How many numbers will be processed? '))
numbers = []
for i in range(1, count + 1):
    value = float(input(f'Enter number {i}: '))
    numbers.append(value)

print(f'The numbers are: {numbers}')  
if count == 0:
    print('The average is not defined for an empty list.')
else:
    average = sum(numbers) / count
    print(f'The average is {average}.')
    
    if average > 0:
        print('The average is positive.')
    elif average < 0:
        print('The average is negative.')
    else:
        print('The average is zero.')
    
    

    