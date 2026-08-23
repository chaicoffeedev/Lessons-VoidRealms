#Functions and arguments

#Function in an argument
def test(name, age, pet):
  print(f'Name = {name}')
  print(f'Age = {age}')
  print(f'Pet = {pet}')

def getData():
  return dict(name='John', age=32, pet='Cat')

d = getData()
test(d['name'], d['age'], d['pet'])

test(**getData())

#Function as an argument
def funky(data):
  print('----Inside funky----')
  d = data()
  print(d)
  print(f'Name = {d["name"]}')
  print(f'Age = {d["age"]}')
  print(f'Pet = {d["pet"]}')

funky(getData) # We are not calling the function,just passing it