#Import madness

#__init__
# What is it, why do we need it

#Makee a sub folder
#Add the files /code

# import sub.test as code
# code.doTest()

#Imports
from sub import *
from sub import test as code

#Call the code
def main():
  print('This is the main function')
  doTest() #Directly call the function as import *
  code.doTest() #Indirectly call the function using 'code' name

if __name__ == "__main__":
  main()