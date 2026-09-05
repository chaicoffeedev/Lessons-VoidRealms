#Multiple Inheritance

#Inherit from multiple classes at the same time

#Vehicle Class
class Vehicle:
  speed = 0
  def drive(self, speed):
    self.speed = speed
    print('Driving')

  def stop(self):
    self.speed = 0
    print('Stopped')

  def display(self):
    print(f'Driving at {self.speed} speed')

#Freezer Class
class Freezer:
  temp = 0
  def freeze(self, temp):
    self.temp = temp
    print('Freezing')

  def display(self):
    print(f'Freezing at {self.temp} temp')

#Freezer Truck Class
class FreezerTruck(Vehicle, Freezer): #here we define the Method Resolution Order MRO
  def display(self):
    print(f'Is a freezer: {issubclass(FreezerTruck, Freezer)}')
    print(f'Is a vehicle: {issubclass(FreezerTruck, Vehicle)}')
    print(f'Self : {self}')

    #super(Vehicle, self).display() #Works beacuse of MRO
    #super(Freezer, self).display() #Fails because of MRO

    Freezer.display(self)
    Vehicle.display(self)

t = FreezerTruck()
t.drive(50)
t.freeze(-30)
print('-' * 20)
t.display()