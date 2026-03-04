hours = float(input('Enter hours worked: '))
rate = float(input('Enter hourly rate: '))
if hours <= 40:
    wage = hours * rate
elif hours <= 50:
    extra_hours = hours - 40 
    wage = (40 * rate) + (extra_hours * rate * 1.5) 
else:
    extra_hours = hours - 40
    wage = (40 * rate) + (extra_hours * rate * 1.5) + 50
    
    
print(f'Weekly wages for {hours:.2f} hours at an hourly rate of ${rate:.2f} per hour is ${wage:.2f}')
    
 