PROMPT = input('Enter daily rainfall values separated by commas: ')
piece = PROMPT.split(",")
rainfall_values = []
for piece in piece:
    piece = piece.strip()  # remove spaces
    if piece != "":
        rainfall_values.append(float(piece))
print(f'The rainfall values are: {rainfall_values}')
if len(rainfall_values) == 0:
    print('Rainfall data is not available.') 
else:
    total_rainfall = sum(rainfall_values)
    average = total_rainfall / len(rainfall_values)
    print(f'Total rainfall is {total_rainfall:.2f}')
    print(f'Average rainfall is {average:.2f}')