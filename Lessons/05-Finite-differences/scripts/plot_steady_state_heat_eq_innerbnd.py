import numpy as np
import matplotlib.pyplot as plt
import sys


### Plot the analytical solution of the heat equation
#    * Steady-state
#    * No advection
#    * Constant heat conductivity
#    * Constant heat production
#
# Choosable Dirichlet + von Neumann boundary conditions
#  T=T0 at z=z1
#  q=q0 at z=z2


###### Start configurable parameters ######

# Define heat conductivity, W/mK
k = 2.5

# Define heat production rate, W/m^3
A = 1.11e-6 #1.8e-6

### Define boundary condition value
# location and value of boundary condition one (von neumann)
z1 = 0.0 #40000.0
q0 = 60.0e-3 #15e-3
# location and value of boundary condition two (dirichlet)
z2 = 0.0
T0 = 0 #20.0

# Define height of the model, meters
L = 40000.0

# Define the x-axis limits of the plot
xlimits = (0.0, 1000.0)

###### End of configurable parameters ######


### Main program:

# Calc depth range for the plot 
N = 100 # num of points we use for plotting
z = np.linspace(0, L, N)

# Calculate integration constants
Ca = q0 + A*z1
Cb = -q0 * z2 - A*z1*z2 + k*T0 + 0.5*A*z2**2

### Evaluate temperature at chosen range
T = (- 0.5 * A * z**2 + Ca*z + Cb) / k

# Generate line to plot the temperature gradient (dT/dz = q/k) at the bottom boundary
Tbot_grad = [T[N-1], T[N-1] - ( k*(T[N-1]-T[N-2])/(z[N-1]-z[N-2]) )*(L/3.0)/k]
zbot_grad = [-z[N-1], -z[N-1] + (L/3.0)]

# Plot the geotherm
plt.figure()
plt.plot(T, -z, "-b")   # T on horizontal axis, z on vertical, pointing down (minus sign), blue solid line
plt.plot(Tbot_grad, zbot_grad, "--r")  # Plot the temperature gradient at the bottom boundary, dashed red line
plt.xlabel("Temperature (deg C)")
plt.ylabel("Depth (m)")
plt.title("Geotherm")
plt.grid()
plt.xlim(xlimits)

plt.show()

