#Iterators
#Making counting easy

t = (1, 2, 3, 4)
for x in t:
  print(x)

"""
Iter basics
Lists, tuples, dictionaries and sets are all iterable objects
They are iterable containers which you can get an iterable form
"""

people = ['John', 'Sam', "Alice", 'Nick']
i = iter(people)
print(i)
print(next(i))
print(next(i))
print(next(i))
print(next(i)) #Stop Iteration

#Iterable class
import random
class Lotto:
  def __init__(self):
    self._max = 5

  """
  The yield statement suspends function's execution
  and sends a value back to the caller , but retains enough
  state to enable function to resume where it is left off
  """
  def __iter__(self):
    for _ in range(self._max):
      yield random.randrange(0, 100)

  def setmax(self, value):
    self._max = value

print('~' * 20)
lotto = Lotto()
lotto.setmax(10)

for x in lotto:
  print(x)

print('~' * 20)
