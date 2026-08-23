#Class Inheritance

#Feline Class
class Feline:
  def __init__(self, name):
    self.name = name
    print('Creating a feline')

  def meow(self):
    print(f'{self.name}: meow')

  def setName(self, name):
    print(f'{self} setting name: {name}')
    self.name = name

#Lion Class
class Lion(Feline):
  def roar(self):
    print(f'{self.name} roar')

#Tiger class
class Tiger(Feline):
    #Overriding the Constructor
    def __init__(self):
    #Super allows it to access to the parent
      super().__init__('No name')
      print('Creating a Tiger')

    def stalk(self):
      print(f'{self.name}: stalking')

    def rename(self, name):
      super().setName(name)


c = Feline('kitty')
print(c)
c.meow()

l = Lion('Leo')
print(l)
l.meow()
l.roar()

t = Tiger() #is a Feline but with a different constructor
print(t)
t.stalk()
t.rename('Tony')
t.meow()
t.stalk()