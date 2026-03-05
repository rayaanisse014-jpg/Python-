PROMPT = 'What is the daily rainfall (negative value to quit)? '
total_rainfall = 0.0
number_of_days = 0
daily_rainfall = float(input(PROMPT))
while daily_rainfall >= 0:

    total_rainfall += daily_rainfall
    number_of_days += 1
    daily_rainfall = float(input(PROMPT))  
if number_of_days == 0:
    print('Rainfall data is not available.')
else:
    average_rainfall = total_rainfall / number_of_days
    print(f'Total rainfall is {total_rainfall:.2f}')
    print(f'Average rainfall is {average_rainfall:.2f}')
      