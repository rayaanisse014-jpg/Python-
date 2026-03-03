first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))
third_number = float(input('Enter the third number: '))
print(f'Evaluating {first_number:.2f}, {second_number:.2f}, and {third_number:.2f}')
if (first_number <= second_number <= third_number) or (third_number <= second_number <= first_number):
    middle = second_number
elif (second_number <= first_number <= third_number) or (third_number <= first_number <= second_number):
    middle = first_number
else: 
    middle = third_number
print(f'The middle number is {middle:.2f}')
