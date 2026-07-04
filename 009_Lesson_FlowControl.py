#IF ELSE ELIF
#Simple Flow Control

#IF Condition
x = False
if x:
  print('yes')
  print('again')
else:
  print('Else Scope')

#Condition evaluations (True - Run | False - Not Run)
x = 100
y = 25
if y == x: print('Equal To')
if y != x: print('Not Equal To')
if y < x: print('Less Than')
if y > x: print('Greater Than')
if y <= x: print('Less Than Equal To')
if y >= x: print('Greater Than Equal To')


print('-----------------------')
#Elseif is the switch solution
x = 75
if x == 25:
  print('x = 25')
elif x == 50:
  print('x = 50')
elif x == 75:
  print('x = 75')
elif x == 100:
  print('x = 100')
else:
  print('Catch all here')

print('-----------------------')
#Nested statements
x = 82
if x > 50:
  print('Over 50')
  if x > 60:
    print('Over 60')
    if x > 70:
      print('Over 70')
      if x > 80:
        print('Over 80')
        if x > 90:
          print('Over 90')
          if x >= 100:
            print('Over 100')