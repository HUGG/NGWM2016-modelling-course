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
H = 2.0e-6

# Define bottom heat flow, W/m^2
q = 20e-3

# Define surface temperature
Tsurf = 20.0

# Define the x-axis limits of the plot
xlimits = (0.0, 1000.0)

# Define depth range for the plot 
# from 0 km to 30 km
z = np.linspace(0, 30000, 100)

# Evaluate temperature at chosen range
T = q*z/k + 30000.0 * H*z/k + Tsurf - 0.5*H*z**2 / k

# Generate line to plot the temperature gradient (dT/dz = q/k) at the bottom boundary
Tbot_grad = [T[99], T[99] - q*10000.0/k]
zbot_grad = [-z[99], -z[99] + 10000.0]

# Plot the geotherm
plt.figure()
plt.plot(T, -z, "-b")   # T on horizontal axis, z on vertical, pointing down (minus sign), blue solid line
plt.plot(Tbot_grad, zbot_grad, "--r")  # Plot the temperature gradient at the bottom boundary, dashed red line
plt.xlabel("Temperature (deg C)")
plt.ylabel("Depth (m)")
plt.title("Geotherm")
plt.grid()
plt.xlim(xlimits)

print T[-1]
plt.show()

