#Basic strings operations

str = "Hello World, this is a string!"


print(len(str)) #Get the length
print(str * 3) #Repeat a string
print(str.replace('Hello', 'Hola')) #Replace
print(str.split(' ')) #Split
print(str.startswith('H'))
print(str.endswith('!'))
print(str.upper())
print(str.lower())
print(str.capitalize())

#Slicing or getting a sub string
print(str[0:5]) # Get the first 5 characters
print(str[6:]) # Get the string from the 6th character to the end
print(str[-7:]) # Get the last 7 characters
print(str[6:11]) # Get the string from the 6th to the 10th character

#indexes - the position of a character in a string
l = ','
c = str.find(l) #Get the index or -1 if not found
print(f'Find returned {c}')

i = str.index(l)
print(f'Index returned {i}') #Get the index or raise an error if not found

x = str[:i]
print(x)