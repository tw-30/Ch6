'''This for statement makes k = variable of the names of each day  
v is the variable for the items inside each dictionary bracket
the print statement makes k(day of the week) then sets it to adding the 3 values together (v), 
and then dividing by the length of the dictionary bracket which each entry has a length of 3 '''

temperatures = {
    'Monday': [66, 70, 74],
    'Tuesday': [50, 56, 54],
    'Wednesday': [75, 80, 83],
    'Thursday': [67, 74, 81]
}

for k, v in temperatures.items():
    print(f'{k}: {sum(v)/len(v):.2f}')
