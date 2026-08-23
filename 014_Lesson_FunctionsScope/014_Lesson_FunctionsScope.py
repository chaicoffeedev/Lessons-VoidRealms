#Lexical scoping

#Global Scope
name = 'John Doe'

#Functions can access the global scope
def test1():
    print(f'My name is {name}')

test1()

#Global scope cannot access function scope
x = 10
def test2():
    x = 50
    print(f'Function scope {x}')

test2()
print(f'Global scope {x}')

#Global > function > statement
x = 15
print(f'Global x: {x}')
def test3():
    x = 0
    print(f'Function x: {x}')
    for i in range(3):
        x += 1
        y = x * i
        print(f'Statement x: {x}')
        print(f'Statement y: {y}')
    print(f'Function x: {x}')
    print(f'Function y: {y}')

test3()
print(f'Global x: {x}')
#print(f'Global y: {y}')

#Functions do not share scope with each other
def cats():
    z = 1 #Only exits in this function

def dogs():
    z = 3 #Only exits in this function

#Functions can return values
def numbers(steps):
    l = range(1, 20, steps)
    for i in l:
        print(i)
    return l

def lotto():
    z = numbers(3)
    for x in z:
        print(f'Lucky number {x}')

lotto()