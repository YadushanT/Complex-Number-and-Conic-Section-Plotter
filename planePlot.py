import matplotlib.pyplot as plt
import numpy as np
import random

figure = plt.figure()
graph = figure.add_subplot(111, projection='3d')  # Creates the 3d plot

temperature, humidity = np.meshgrid(range(20), range(20))
pressure = 1 - temperature + 2 * humidity  # The given plane equation

graph.plot_surface(temperature, humidity, pressure, alpha=0.4)

# Labelling the axes
plt.xlabel('x-axis')
plt.ylabel('y-axis')
graph.set_zlabel('z-axis')

#initializing arrays to store the values for the points
point = []
point2 = []
for i in range(3):  # Randomly generates the x, y, and z values for two points
    point.append(round(random.uniform(0, 10), ndigits=1))
    point2.append(round(random.uniform(0, 10), ndigits=1))

print('Point One: {point}')
print('Point Two: {point2}')
graph.scatter(point[0], point[1], point[2], color='blue')  # Graphs point one
graph.scatter(point2[0], point2[1], point2[2], color='blue')  # Graphs point two
plt.show()


