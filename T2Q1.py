first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))
average = (first_number + second_number) / 2
print(f'The average of {first_number} and {second_number} is {average}.')

if average > 0:
    print('The average is positive.')
elif average < 0:
    print('The average is negative.')
else:
    print('The average is zero.')