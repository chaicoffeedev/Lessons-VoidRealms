"""
***** Decorators *****
Everything in python is an object
That means functions can be used as obejcts
So we can do some really cool things
A decorator takes in a function, adds some additional functionality and returns it.
"""

#Basic Decorator
#In this example we will change the execution order

def test_decorator(func):
  print('Before')
  func()
  print('After')

@test_decorator
def do_stuff():
  print('Doing stuff')

#Verbose mode for passing a function to another function
#f = test_decorator(do_stuff)


#Real decorator
#In this example, we will change the functionality
# @makeBold is equal to
# f = makeBold(printName)
# f()
def makeBold(fun):
  def inner():
    print('<b>')
    fun()
    print('</b>')
  return inner #return the inner function

@makeBold
def printName():
  print('John Doe')

printName()

#Decorator with params
#Notice this has a defined no. of params

def numcheck(func):
  def checkInt(o):
    if isinstance(o, int):
      if o == 0:
        print('Cannot divide by zero')
        return False
      return True
    print(f'{o} is not a number')
    return False

  def inner(x, y):
    if not checkInt(x) or not checkInt(y):
      return
    return func(x,y)
  return inner

@numcheck
def divide(a, b):
  print(a/b)

divide(100, 3)
divide(100, 0)
divide(100, 'cat')

#Decorators with unknown no. of params
#We want a decorator that can pass params and handle anything
#We also want to chain them together
# *args, **kwargs to the rescue

def outline(func):
  def inner(*args, **kwargs):
    print('-' * 20)
    func(*args, **kwargs)
    print('-' * 20)
  return inner

def list_items(func):
  def inner(*args, **kwargs):
    func(*args, **kwargs)
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')
    for x in args:
      print(f'arg={x}')
    for k,v in kwargs.items():
          print(f'key={k}, value={v}')
  return inner

@outline
@list_items
def display(msg):
  print(msg)

display('Hello World')

@outline
@list_items
def birthday(name='', age=0):
  print(f'Happy Birthday {name} you are {age} years old!')

birthday(name='John', age=32)