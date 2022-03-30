tlds = {'Canada':'ca', 'United States':'us', 'Mexico':'mx'}

#a
#check if dictionary contains canada 
if 'Canada' in tlds:
    print("Canada is in this dictionary.")
    print('-------------------------')

#b
#check france in dictionary
if 'France' not in tlds:
    print('France is not in this dictionary')
    print('-------------------------')
    

#c
#iterate through key-value pairs, display in 2 column 
print("{:<15} {:<5}".format('Country', 'TLDs'))

#for loop if pair in tlds
for key, name in tlds.items():
    print("{:<15} {:<5}".format(key, name))
print('-------------------------')


#d
#wrong abbrev
tlds['Sweeden'] = 'sw'
print(tlds)
print('-------------------------')
#e
#right abbrev/update abbrev
tlds['Sweeden'] = 'se'
print(tlds)
print('-------------------------')


#f
#use dict comprehension to reverse keys and values 
tlds = {name : key for (key, name) in tlds.items()}
print(tlds)
print('-------------------------')


#g
#use part f to convert country names to uppercase 
tlds = {key: name.upper() for (key, name) in tlds.items()}
print(tlds)