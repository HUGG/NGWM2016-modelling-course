import numpy as np
import matplotlib.pyplot as plt
import sys


### Plot the analytical solution of the heat equation
#    * Steady-state
#    * No advection
#    * Constant heat conductivity
#    * Constant heat production
#
# Choosable boundary conditions
#  - Fixed surface temperature
#  - Bottom heat flux or bottom temperature defined


###### Start configurable parameters ######

# Define heat conductivity, W/mK
k = 2.5

# Define heat production rate, W/m^3
H = 2.0e-6

# Choose type of bottom boundary condition
bottom_bnd_cond_type = "dirichlet"  # can be "vonneumann" or "dirichlet"

### Define value of the bottom boundary condition
# For von Neumann: Define bottom heat flow, W/m^2
qb = 20e-3
# For Dirichlet: Define bottom boundary temperature, deg C
Tbott = 600.0

# Define surface temperature
Tsurf = 20.0

# Define height of the model, meters
L = 30000.0

# Define the x-axis limits of the plot
xlimits = (0.0, 1000.0)

###### End of configurable parameters ######


### Main program:

# Calc depth range for the plot 
N = 100 # num of points we use for plotting
z = np.linspace(0, L, N)

# Calculate integration constants
if bottom_bnd_cond_type == "vonneumann":
  Ca = qb + H*L
  Cb = -k*Tsurf
elif bottom_bnd_cond_type == "dirichlet":
  Ca = (k*Tbott + 0.5*H*L**2 - k*Tsurf) / L
  Cb = Tsurf*k
else:
  print("Invalid bottom boundary condition type " + bottom_bnd_cond_type)
  print("Adjust parameter bottom_bnd_cond_type")
  dummy = raw_input("Press enter to quit")
  sys.exit(1)

### Evaluate temperature at chosen range
T = (- 0.5 * H * z**2 + Ca*z + Cb) / k

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

