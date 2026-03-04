number = int(input('Enter a positive integer: '))
original_number = number
reserved_number = 0
while number > 0:
    last_digit = number % 10
    reserved_number = reserved_number * 10 + last_digit
    number = number // 10
    
print(f'The reverse of {original_number} is {reserved_number}.')