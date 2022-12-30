'''
This is the function for calculating the 
adult height from the height of their parents
'''

# Create input parameter setting
father = float(input("Please Input father's height in cm = "))
mother = float(input("Please Input mother's height in cm = "))
sex = str(input("Please Input Sex (Boy or Girl): "))

# Function to calculate height
if sex == 'Boy':
    adult_height = (father + mother)/2 + 6.5
if sex == 'Girl':
    adult_height = (father + mother)/2 - 6.5

print('The adult height is ' + str(adult_height) + 'cm.')

  
 
