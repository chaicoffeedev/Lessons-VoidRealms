#Working with binary files

#Imports
import random
import operator

#Create random bytes
def randomBytes(size):
  bytes = []
  for x in range(size):
    bytes.append(random.randrange(0,255))
  return bytes

def displayBytes(bytes):
  print("-" * 20)
  for index, item in enumerate(bytes, start=1):
    print(f'{index} = {item} ({hex(item)})')
  print("-" * 20)

# b = randomBytes(10)
# displayBytes(b)

#Write bytes
def writeBytes(filename, bytes):
  with open(filename, 'wb') as file:
    for b in bytes:
      file.write(b.to_bytes(1, byteorder='big'))

#Read bytes
def readBytes(filename):
  bytes = []
  with open(filename, 'rb') as file:
    while True:
      b = file.read(1)
      if not b:
        break
      bytes.append(int.from_bytes(b, byteorder='big'))
  return bytes

#See it in action

#Create the random bytes
outbytes = randomBytes(10)
displayBytes(outbytes)

#Write bytes
filepath = 'testBinary.dat'
writeBytes(filepath, outbytes)

#Read bytes
inbytes = readBytes(filepath)
displayBytes(inbytes)
print(f'Match: {operator.eq(outbytes, inbytes)}')