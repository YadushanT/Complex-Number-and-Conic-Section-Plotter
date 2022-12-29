import numpy as np
import matplotlib.pyplot as plt


x_min, x_max, x_samples = (-6, 6, 200) #setting the parameters for horizantal portion of the graph
y_min, y_max, y_samples = (-10, 10, 200) #setting the parameters for vertical portion of the graph
x = np.linspace(x_min, x_max, x_samples) #makes the markers along the x axis equidistant from each other
y = np.linspace(y_min, y_max, y_samples) #makes the markers along the y-axis equidistant from each other
x_mesh, y_mesh = np.meshgrid(x, y) #creates the rectangular grid

#equation for the lines
plt.contour(x_mesh, y_mesh, x_mesh**2 - y_mesh, [4])
plt.contour(x_mesh, y_mesh, 2*x_mesh**2 - y_mesh, [4])
plt.contour(x_mesh, y_mesh, 3*x_mesh**2 - y_mesh, [4])

plt.xlim((x_min, x_max)) #sets the x-limits of the x-axis
plt.xlabel(x) #labels the x-axis
plt.ylim((y_min, y_max)) #sets the y-limits of the y-axis
plt.ylabel(y) #labels the y-axis
plt.show() # opens the window to display our plots

