# -*- coding: utf-8 -*-
        
import math

# decreased 1e-5 to 1e-9 to calculate roots to 8 decimal places (tolerance)
eps_abs = 1e-9
eps_step = 1e-9

# since root 3 is between 1 and 2, interval is [1,2]
a = 1
b = 2


def f(x):
    return x**2 - 3


iterations = 0  # declare variable iterations = 0 to count number of iterations

# print table
print("------------------------------------------------")
print("Iterations | Estimated Value | Estimated Error |")
print("------------------------------------------------")

while ((b-a) >= eps_step) or (abs(f(a) >= eps_abs) and abs(f(b) >= eps_abs)):
    c = (a+b)/2
    if (f(a)*f(c) < 0):
        b = c
    else:
        a = c
    iterations += 1 # add 1 to iteration number
    print("{:^11.0f}|{:^17.8f}|{:^17.9f}|".format(iterations, c, math.sqrt(3) - c)) # print iterations, estimated value, and estimated error in the format of a table
    if (round(math.sqrt(3) , 8) == round(c, 8)): # if root is found to 8 decimal places, then breaks out of loop
        break

print('\n')
print('Square root 3: ' + str(round(math.sqrt(3), 8))) # print root 3 to 8 decimal places
print('Iterations: ' + str(iterations)) # print number of iterations
