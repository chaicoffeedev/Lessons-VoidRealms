#For loop and range

#For loop on lists, tuples, sets
l = [1,2,3,4] #List
t = (1,2,3,4) #Tuple
s = {1,2,3,4} #Set

for i in s:
  print(f'i = {i}')

#For loop in dictionaries
x = dict( Bob=32, Alice=35, John=21, Macy=18 )
print(x)

#Using keys to find values from dictionary
for k in x.keys():
  print(f'Keys: {k} = {x[k]}')

for k,v in x.items():
  print(f'Items: {k} = {v}')

#Range
x = range(5)
print(x)
for i in x:
  print(f'Range = {i}')

#Range start, stop and step
x = range(5, 20, 3)
print(x)
for i in x:
  print(f'Stepped: {i}')