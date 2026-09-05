#The underscore
#Often ignored, multiple uses
#_Single
#__Double
#__Before
#After__
#__Both__

#Skipping
# Underscore _ here is the default local variable in the for loop scope
for _ in range(5): 
  print(f'Hello {_}')

#Test class
from person import *

#Before (Single)
#Internal use only, called a weak private
p = Person()
p.setName('John')
print(f'Weak private {p._name}')
p._name = 'NOOOOOO'
print(f'Weak private {p._name}')

#Before (Double)
#Internal use only, avoids conflict in subclass
#and tells python to rewrite the name (mangling)
p = Person()
p.work()
#p.__think()
#c = Child()
#c.testDouble()


#After (Any)
#Helps avoid naming conflicts with keywords using the underscore symbol
class_ = Person()
print(class_)

#Before & After underscore
#Considered special to Python, like the init and main function
p = Person()
p.__call__()
