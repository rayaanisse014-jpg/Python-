from math import floor
raw_mark = float(input('Enter the final percentage mark: '))
rounded_mark = floor(raw_mark + 0.5)
print(f'The raw mark of {raw_mark}% rounds off to {rounded_mark}%')
if rounded_mark < 0 or rounded_mark > 100: 
    print('That mark is invalid.')
else:
    if rounded_mark >= 85:
        grade = 7 
    elif rounded_mark >= 75:
         grade = 6
    elif rounded_mark >= 65:
         grade = 5
    elif rounded_mark >= 50:
         grade = 4
    elif rounded_mark >= 40:
        grade = 3
    elif rounded_mark >= 25:
        grade = 2
    else:  
        grade = 1
    print(f'A score of {rounded_mark}% gives a grade of {grade}.')
        
    
        
