#Lesson 3, Basics of Python Strings

for x in 'hello':
  print(f'{x} = {ord(x)}')

#Create strings
first = "Bryan" #Can be double quotes
last = 'Cairns' #Can be single quotes
print(first + ' ' + last)
print(f'Hello my anme is {first} {last}') #Tend to use formatted to avoid issues

hers = "Heather's"
print(hers)

#Under the hood, string is a unified set of UTF8 characters

s1 = chr(72)  #Display the utf-8 code as character
s2 = chr(105)
print(s1 + s2)
print(chr(8710)) #Way beyond the ascii code

#Escape characters - start with a slash \
print(f'Hello{chr(13) + chr(10)}World')
print(f'Hello\r\nWorld')
strTest = "Hello\tWorld"
print(strTest)

hers = 'Heather\'s'
print(hers)

quote = "Then he said \"hello\" to me"
print(quote)

#Must format strings to avoid errors

name = "Bryan"
age = 30

#print(name + ' ' + age) Error!!!

print(f'My name is {name} I am {age}')
print("My name is %s, I am %i years old" %(name, age))