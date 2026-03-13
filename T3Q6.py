number_text = input('Enter a positive integer: ')
digits = []
for char in number_text:
    digits.append(int(char))
reversed_digits = []
for i in range(len(digits) - 1, -1, -1):
    reversed_digits.append(digits[i])
weighted_digits = []
for i in range(len(reversed_digits)):
    weighted_digits.append(reversed_digits[i] * (i + 1))
print(f'The digits are: {digits}')
print(f'The reversed digits are: {reversed_digits}')
print(f'The weighted reversed digits are: {weighted_digits}')