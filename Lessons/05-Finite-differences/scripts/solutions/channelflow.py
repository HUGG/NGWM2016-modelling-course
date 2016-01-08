import numpy as np
import matplotlib.pyplot as plt
from analytical_solutions import *



eta = 1.0     # viscosity, Pa s
Pgrad = 0.0
ny = 10
h = 1.0


# Create grid
y = np.zeros(ny)
dy = h / (ny - 1)
for i in range(0,ny):
  y[i] = i*dy

# Create an velocity array
u = np.zeros(ny)

u[0] = 1.0
u[1] = 1.0

# Calculate values
for i in range(2, ny):
  u[i] = dy**2 * Pgrad / eta + 2*u[i-1] - u[i-2]
  
plt.plot(u, -y)    # y axis points down -> minus sign
plt.xlabel("u")
plt.ylabel("y")
plt.show()




