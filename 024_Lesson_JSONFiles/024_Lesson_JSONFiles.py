#JSON Files
#App to app communication

"""
{
  "name" : "John",
  "age" : 30,
  "pet" : "cat"
}
"""

#Imports
import json
filename = 'test.json'

#To string
outD = dict(name = "John", age = 30, pet = "cat")

s = json.dumps(outD) #Dumps put it to a string
print(f'String={s}')

#To file
with open(filename, 'w') as f:
  json.dump(outD, f) #Dump put it to a file

#From string
inD = json.loads(s) #Loads the dictionary from the string
print(f'Dictionary={inD}')

#From file
with open(filename, 'r') as f:
  fD = json.load(f)
print(f'Type: {type(fD)} = {fD}')