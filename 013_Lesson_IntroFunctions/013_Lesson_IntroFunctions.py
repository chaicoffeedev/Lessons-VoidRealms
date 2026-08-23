#Intro to functions

#Define a function
def test():
    print("This is a function.")

#Define a fucntion with parameters and return a value
def sqft(w, h):
    v = w * h
    return v

#Call a fucntion
test()

#Call a function multiple times
for x in range(4):
    test()

#Call a function with parameters
x = sqft(12, 8)
print(f'The square footage is {x}')