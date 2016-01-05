import numpy as np
import matplotlib.pyplot as plt


### Plot the analytical solution of the heat equation
#    * Steady-state
#    * No advection
#    * Constant heat conductivity
#    * Constant heat production

### Plot the geotherm

# Define heat conductivity, W/mK
k = 2.5

# Define heat production rate, W/m^3
H = 3e-6

# Define depth range for the plot 
# from 0 km to 30 km
z = np.linspace(0, 30000, 100)

# Evaluate temperature at chosen range
T = -(1.0/(2.0*k)) * H * z**2 + (58.0/3000.0) * z + (1.0/(2.0*k))*30000.0 * H * z  + 20.0

# Plot the geotherm
plt.figure()
plt.plot(T, -z)   # T on horizontal axis
                  # z on vertical, pointing down (minus sign)
plt.xlabel("Temperature (deg C)")
plt.ylabel("Depth (m)")
plt.title("Geotherm")

print T[-1]
plt.show()

