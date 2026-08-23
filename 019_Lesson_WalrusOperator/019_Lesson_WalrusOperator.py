#Walrus operator and global
#Added in Python 3.8 looks like :=

#Assign a variable from an expression
#must have the right version!

#Common issues
#y := len('hello') #Invalid syntax
(y := len('hello')) #Valid syntax but not recommended
print(y)

people = ['John', 'Sammy','Joe']
if n:= len(people) <= 3: print(n)
if (n:= len(people)) <= 3: print(n)

#Simple example
lines = []

""" def canAdd(max = 5):
  global lines #Allows us to use global variable
  if allowed := (count := len(lines)) < max:
    print(f'You can enter {max - count} more')
  return allowed

while canAdd():
  lines.append(l := input('Enter a line:'))

print(f'You entered: {lines}') """

print('-------Bro Code Lectures-------')
#happy = True
print(happy := True) #Inplace variable creation and assignment from an expression
happy = False

# foods = list()
# while True:
#   food = input("What food do you like?: ")
#   if food == "quit":
#     break
#   foods.append(food)

#We implement the same program using the Walrus (:=) operator

foods = []
while food := input("What food do you like?: ") != "quit":
  foods.append(food)