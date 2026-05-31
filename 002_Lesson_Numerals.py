#Lesson 2, Basics of Python Numerals System
import sys
#Numbers -> int, float and complex 

#int 
ival = 34
print(f'ival = {ival}')
#print(type(ival))


#float
fval = 3.15
print(f'fval = {fval}')
#print(type(fval))
print(sys.float_info)

#complex
cval = 3 +6j
print(f'cval = {cval}')
#print(type(cval))

cval = complex(5, 3)
print(f'cval real = {cval.real}, imag = {cval.imag}')



#basic numerical operation
x = 3
print(f'x = {x}')

y = x + 4 #add
print(f'add = {y}')

y = x - 1 #subtract
print(f'subtract = {y}')

y = x * 6.846 #multiply
print(f'multiply = {y}')

y = x / 0.5 #divide
print(f'divide = {y}')

y = x ** 2 #pow
print(f'pow = {y}')

y = x % 2.5 #remiander
print(f'remainder = {y}')