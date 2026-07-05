#Simple app - Paint Calculator

print('Paint Calculator')
print('Enter a wall size as width, height in feet or Press Enter to stop')
print('Example: 12,8')

#Variables
walls = [] #List of walls measurements
gallons = 1 / 350 #One gallon covers 350 sqft
total = 0 #Total gallons to buy

#Get the user input
while True:
  s = input('Enter a wall size:')
  if len(s) == 0: break

  #Verify the input
  sqft = s.split(',')
  if len(sqft) < 2:
    print('Invalid format')
    break