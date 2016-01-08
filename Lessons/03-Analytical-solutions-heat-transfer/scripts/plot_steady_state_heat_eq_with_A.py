import numpy as np
import matplotlib.pyplot as plt


### Plot the analytical solution of the heat equation
#    * Steady-state
#    * No advection
#    * Constant heat conductivity
#    * Constant heat production
#
# Fixed boundary conditions
# T=20 at z=0
# T=600 at z=30km

### Plot the geotherm

# Define heat conductivity, W/mK
k = 2.5

# Define heat production rate, W/m^3
A = 3e-6

# Define depth range for the plot 
# from 0 km to 30 km
z = np.linspace(0, 30000, 100)

# Evaluate temperature at chosen range
T = -(1.0/(2.0*k)) * A * z**2 + (58.0/3000.0) * z + (1.0/(2.0*k))*30000.0 * A * z  + 20.0

# Plot the geotherm
plt.figure()
plt.plot(T, -z)   # T on horizontal axis
                  # z on vertical, pointing down (minus sign)
plt.xlabel("Temperature (deg C)")
plt.ylabel("Depth (m)")
plt.title("Geotherm")

plt.show()

