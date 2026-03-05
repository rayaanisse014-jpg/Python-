number = int(input('Enter a positive integer: '))
original_number = number
running_total = 0
while number > 0:
    # Get the last digit
    last_digit = number % 10
     #Add it to the running total
     # running_total + running_total + last_digit 
    running_total += last_digit 
    # Remove the last digit
    number = number // 10
print(f'The sum of the digits in {original_number} is {running_total}.') 