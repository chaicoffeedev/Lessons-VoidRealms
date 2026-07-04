#Sets {}
#Sets contain unordered, unique, immutable data types in a hash table

#Creating a set
s = {1, 2, 2, 2, 3, 4, 5}
print(s)

l = ['Adam', 'Eve', 30]
s = set(l)
print(s)

#Adding items
s.add('Hello')
s.update([1, 2, 3, 'Hello'])
print(s)

#Removing items
s.discard('Hello') #Will not throw an error
s.remove(1) #Will throw an error if item is not present
v = s.pop() #Pop removes a values and gives it to you
print(s)

#Cannot change items 
#s[0] = 'A' #Error
#print(s[0]) #Error

print(3 in s)
s.remove(3)
s.add(12)
print(s)

x = set('abcd')
y = set('cdefg')

s = x.union(y) #All the elements that are in either set
print(f'Union {s}')

s = x.intersection(y) #All the elements that are common in both sets
print(f'Inersection {s}')

s = x.difference(y) #All the elements that are in x but not in y
print(f'Difference {s}')

s = y.difference(x) #All the elements that are in y but not in x
print(f'Difference {s}') 

s = x.symmetric_difference(y) #All the elements that are in one of the sets
print(f'Symmetric Difference {s}') 