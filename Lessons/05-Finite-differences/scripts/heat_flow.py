import numpy as np
import matplotlib.pyplot as plt

# Finite difference code to solve the equation q = k * dT/dz
# given the boundary condition T=T_surf at the upper boundary



z_surf = 0.0  # location of upper surface
z_bott = 50e3 # location of bottom boundary

nz = 5        # number of grid points

T_surf = 0.0  # temperature of the upper surface
q = 15e-3     # heat flow in the crust (constant throughout)
k = 2.5       # heat conductivity




# Generate the grid
dz = (z_bott - z_surf) / (nz - 1)
z = np.zeros(nz)

for i in range(0, nz):
  z[i] = z_surf + i*dz

print("Grid points are:")
print(z)

# Generate an empty array for temperature values
T = np.zeros(nz)


# Set boundary conditions, i.e. the upper surface temperature
T[0] = T_surf


# Calculate temperature values inside the model
for i in range(1, nz):   # NB! Grid point 0 omitted
                         # as it cannot be calculated
  T[i] = ????


# Print and plot the depth vs temperature
print("Temperature values are:")
print(T)
plt.plot(T, -z, "o-")   # minus sign is placed to make z axis point down
plt.xlabel("Temperature")
plt.ylabel("Depth")
plt.show()


