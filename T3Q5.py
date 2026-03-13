number_text = input('Enter a positive integer: ')

digits = []
for char in number_text:
    digit = int(char)
    digits.append(digit)
print(f'The digits are: {digits}')
multiplier = int(input('Enter the multiplier: '))
scaled_digit = sum(digits) * multiplier
print(f'The scaled digit sum is {scaled_digit}.')