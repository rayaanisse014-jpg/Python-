temperature_in_Fahrenheit = float(input('Enter a temperature in Fahrenheit: '))
Celsius = (5/9) * (temperature_in_Fahrenheit - 32)
print(f'{temperature_in_Fahrenheit:.3f} degrees Fahrenheit is the same as {Celsius:.3f} degrees Celsius.')
if Celsius < 0: 
    print('That is below freezing point.')
elif Celsius == 0:
     print('That is freezing.')
elif Celsius == 100:
    print('That is boiling.')
elif Celsius > 100:
    print('That is above boiling point.')
else:
    print('That is between freezing and boiling.')