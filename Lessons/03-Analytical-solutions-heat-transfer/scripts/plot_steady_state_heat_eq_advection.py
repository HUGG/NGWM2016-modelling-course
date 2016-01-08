import numpy as np
import matplotlib.pyplot as plt
import sys


### Plot the analytical solution of the heat equation
#    * Steady-state
#    * Constant advection velocity
#    * Constant heat diffusivity
#    * Constant heat production
#
# Choosable boundary conditions
#  - Fixed surface temperature T=0
#  - Fixed bottom temperature T=Tbott

###### Start configurable parameters ######

# Define heat conductivity, W/mK
k = 2.5

# Define volumetric heat production rate, W/m^3
A = 0

# Define advection velocity, m/s
# NB! z axis points down, so negative velocity points up
uz = 5 / (1000 * 60 * 60 * 24 * 365.25)   # scaled from mm/a   

# Define density, kg/m^3
rho = 2800.0

# Define heat capacity, J/kgK
Cp = 850.0 

# Define boundary conditions, q and T defined at common depth z0
Tbott = 600.0

# Define height of the model, meters
L = 40000.0

# Define the x-axis limits of the plot
xlimits = (0.0, 600.0)

###### End of configurable parameters ######


### Main program:

# Calculate diffusivity
kappa = k / (rho * Cp)

# Calc depth range for the plot 
N = 1000 # num of points we use for plotting
z = np.linspace(0, L, N)

# Calculate integration constants
### Evaluate temperature at chosen range
#T = Tbott * (1-np.exp(-uz*z/kappa)) / (1-np.exp(-uz*L/kappa))
T = Tbott * (np.exp(z*uz/kappa)-1) / (np.exp(L*uz/kappa)-1)

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

