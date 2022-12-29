import math


a = 1 #declaring the value for a
b = 9**12 #declaring the value for b
c = 3 #declaring the value for c

#performing quadratic equation
x1 = (-1*b + math.sqrt(b**2 - 4*a*c))/2*a
x2 = (-1*b - math.sqrt(b**2 - 4*a*c))/2*a

#output
print( "Question 4b (METHOD 1)")
print("x1 =" , x1 , "/ x2 =", x2)
print()



if b < 0: #only runs if b<0
    x1 = (-1*b + math.sqrt(b**2 - 4*a*c))/(2*a) #calculation for x1 via quadratic equation
    x2 = c/a/x1 #calculation for x2 by dividing c by a by x1
else: #runs if the first if statement doesn't run
    x2 = (-1*b - math.sqrt(b**2 - 4*a*c))/(2*a) #calculation for x2 via quadratic equation
    x1 = c/a/x2 #calculation for x1 by dividing c by a by x2


print( "Question 4b (METHOD 2)")
print("x1 =" , x1 , "/ x2 =", x2)
print()




