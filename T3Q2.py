dice_values = []
for i in range(1, 6):
    die_number = int(input(f'Enter die {i}: '))
    dice_values.append(die_number)
first_value = dice_values[0]
yahtzee = True
for die_value in dice_values:
    if die_value != first_value:
        yahtzee = False
        break
print(f'The dice are: {dice_values}')
if yahtzee is True:
    print('Congratulations, your score is 50!')
else:
    print('Too bad, you did not get Yahtzee. Better luck next time.')
        
    


    
    