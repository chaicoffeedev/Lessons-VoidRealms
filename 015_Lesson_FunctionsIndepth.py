#Functions in depth

#No arguments
def test():
    print('Normal functions')

print('\r\n------ No arguments')
test()

#Positional and keyword Arguments
def message(name, msg, age):
    print(f'Hello {name}, {msg}, you are {age} years old.')

print('\r\n------ Positional and keyword Arguments')
message('John', 'Good Morning!', 25) #positional 
message('John', 22, 'Good Morning!') #positional (wrong order)
message(msg='Good Morning!', age=46, name='John') #keyword
message('Bryan', age=46, msg='Good Morning!')

#Internal functions
def counter():
    def display(count = 0): #Function in a function
        print(f'Internal: {count}')
    for x in range(5): display(x)

print('\r\n------ Internal fucntions')
counter()


# *args - positional variable length arguments
def multiple(*args):
    z = 1
    for num in args:
        print(f'Num = {num}')
        z *= num
    print(f'Multiply: {z}')

print('\r\n------ *args')
multiple(2, 3, 1, 4, 5, 6, 8, 2, 4, 5, 6)

# **kwargs is used to pass a keyworded, variable length arguments 
def profile(**person):
    print(person)
    def display(k):
        if k in person.keys(): print(f'{k} = {person[k]}')
    display('name')
    display('age')
    display('pet')
    display('pezzzzzzt')


print('\r\n------ **kwargs')
profile(name='John', age=25)
profile(name='John', age=25, pet='Cat')
profile(name='John', age=25, pet='Cat', food='pizza')


#Lambda functions (anonymous fucntions)
print('\r\n------ Lambda')
#normal
def makesqft(width=0, height=0):
    return width * height
print(makesqft(width=10, height=8))
print(makesqft(15, 8))

#lambda
#z = lambda x: x * y
sqft = lambda width=0, height=0: width * height

print(sqft(width=10, height=8))
print(sqft(15, 8))