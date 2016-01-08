import numpy as np
import matplotlib.pyplot as plt

# Finite difference code to solve the steady state geotherm
# given the boundary condition T=T_surf at surface
# and the surface heatflow q.
# Heat generation A is variable and defined in two layers



z_surf = 0.0   # location of upper surface
z_bott = 150e3 # location of bottom boundary

nz = 100        # number of grid points

T_surf = 0.0     # temperature of the upper surface, deg C
q_surf = 50e-3   # surface heat flow, mW/m^2
k = 2.5          # heat conductivity, W/mK

A1 = 1.1e-6     # heat production rate for layer 1
A2 = 0.02e-6    # heat production rate for layer 2
L1 = 35e3       # Thickness of layer one (from surface to L1)
                # Thickness of layer two is calculated
                # and extends from L1 to z_bott



# Generate the grid
# Regular grid is used, so that in FD calculations
# only dz is needed. Array z is used only for plotting.
dz = (z_bott - z_surf) / (nz - 1)
z = np.zeros(nz)

for i in range(0, nz):
  z[i] = z_surf + i*dz

print("Grid points are:")
print(z)


# Generate the material properties array for heat production rate
A = np.zeros(nz)
A[z <  L1] = A1
A[z >= L1] = A2


# Generate an empty array for temperature values
T = np.zeros(nz)



# Set boundary conditions, i.e. the upper surface temperature
# and the temperature at one grid point below
T[0] = T_surf

## Grid point one needs special handling as T[-1] is not available
# Calculate "ghost point" outside the model domain, where grid point -1 
# would be, assuming surface heat flow q_surf
Tghost = T[0] - q_surf * dz / k  # = "T[-1]"
# Use the same finite difference formula to calculate T as for 
# the inner points, but replace "T[-1]" by ghost point value
T[1] = -A[1] * dz**2 / k - Tghost + 2*T[0]


# Calculate temperature values inside the model
for i in range(2, nz):   # NB! Grid points 0 and 1 omitted
                         # as they cannot be calculated
  T[i] = -A[i] * dz**2 / k - T[i-2] + 2*T[i-1]


# Print and plot the depth vs temperature
print("Temperature values are:")
print(T)
plt.plot(T, -z, "o-")   # minus sign is placed to make z axis point down
plt.xlabel("Temperature")
plt.ylabel("Depth")
plt.show()


