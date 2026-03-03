first_die_value = int(input('Enter die 1: '))
second_die_value = int(input('Enter die 2: '))
third_die_value = int(input('Enter die 3: '))
fourth_die_value = int(input('Enter die 4: '))
fifth_die_value = int(input('Enter die 5: '))
print(f'The dice are: {first_die_value}, {second_die_value}, {third_die_value}, {fourth_die_value}, and {fifth_die_value}.')

if first_die_value == second_die_value == third_die_value == fourth_die_value == fifth_die_value:
    print('Congratulations, your score is 50!')
else:
    print('Too bad, you did not get Yahtzee. Better luck next time.')
