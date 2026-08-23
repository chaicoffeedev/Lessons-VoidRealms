#List is a more complex data structure than a variable. 
# It can hold multiple values, and those values can be of different types. 
#Lists are ordered, meaning that the items have a defined order, and that order will not change unless you explicitly change it.
 # Lists []

#Create a list
x = ['John', 'Jane', 46] #Can hold different types of data
print(f'List: {x}')
print(f'Len: {len(x)}')


#Index and positioning - 0 based
print(f'Zero: {x[0]}')
print(f'Slice: {x[1:2]}') #Slice the list

#Adding items
x.append('Pizza') #Add item at the end
x.append('Beer') #Add item at the end
x.insert(1, 'Cats') #Insert item at a specific position
print(f'List: {x}')

#Removing items - remove, pop, delete
x.remove('Cats') #Remove an item
print(f'List: {x}')

i = x.index('Pizza')
print(f'Food: {x.pop(i)}')
print(f'List: {x}')

i = x.index('Beer')
del x[i] # Delete an item without returning it
print(f'List: {x}')

#Extending - Adds elements from another list
y = ['Cats', 'Dogs', 'Birds']
x.extend(y)
print(f'List: {x}')

#Sort - sort, reverse
x.remove(46)
x.sort()
print(f'List: {x}')
x.reverse()
print(f'List: {x}')

#Copy
y = x.copy()
y.reverse()
y.append('Apples')
print(f'Original: {x}')
print(f'New: {y}')

#Delete the whole list
del y

#Clear the list
x.clear()
print(f'Cleared: {x}')
print(f'Len: {len(x)}')

#Lists can contain other lists [[],[],[]] Nested Lists
x = []
y = [1,2,3]
z = ['John', 'Doe']
x.append(y)
x.insert(0, z)

print(f'Lists in List: {x}')
print(f'Len: {len(x)}')
print(f'0: {x[0][0]}')
print(f'1: {x[1][1]}')

#Chnaging items
x = [1,2,3,4,5]
x[2] = 'Test'
print(x)