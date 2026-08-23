#Imports

#Lets make our code usable to other scripts
#This allows us to structure our code and simplify things


#Create the file
#Go ahead and look at 025_zmycode.py

#Import as <make sure to change the name of the file and add z at the beginning>
import mycode as person

#Scope issues
global name
# print(name)
print(person.name) #Each file can and should use its own scope

#Test the code
person.name = 'John'
person.greet()
person.toFile('test.txt')

person.name = 'Alison'
person.greet()

person.fromFile('test.txt')
person.greet()
