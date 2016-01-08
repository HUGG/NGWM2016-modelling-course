import numpy as np
import matplotlib.pyplot as plt
from analytical_solutions import *


z_surf = 0.0  # location of upper surface
z_bott = 150e3 # location of bottom boundary

nz = 11        # number of grid points
nt = 8        # number of timesteps to calculate
dt = 0.5*112500000000000.0 # timestep to use, in seconds

T_surf = 0.0   # temperature of the upper surface
T_bott = 1300.0 # temperature of the lower boundary
T_ini = 1300.0

k = 4.5        # heat conductivity
rho = 3200     # density
Cp = 1250       # heat capacity

plot_every = 1          # plot the temperature field every Nth timestep
plot_analytical = True  # change this to 'False' to omit plotting the analytical solution
                        # Analytical solution is applicable to cooling/heating of the semi-infinite
                        # half-space, i.e. for case T_bott == T_ini != T_surf 




# Generate the grid
dz = (z_bott - z_surf) / (nz - 1)
z = np.zeros(nz)

for i in range(0, nz):
  z[i] = z_surf + i*dz

# Generate array of times at every timestep
# Used only for plotting
t = np.zeros(nt)
for j in range(0, nt):
  t[j] = j*dt

print("Grid points are:")
print(z)

# Generate an empty array for temperature values
# for every grid point at every time step, i.e. an array
# of size nt times nz
T = np.zeros((nt, nz))


# Set initial condition, T=0 everywhere except at boundaries
j = 0  # = initial step
T[j, 0] = T_surf
T[j, nz-1] = T_bott
for i in range(1, nz-1):
  T[j, i] = T_ini

time = 0

# Loop over time steps, skipping the first one (=initial condition)
for j in range(1,nt):
  time = time + dt
  
  # Set boundary condition
  T[j, 0] = T_surf
  T[j, nz-1] = T_bott

  # Calculate temperature at inner grid points
  for i in range(1, nz-1):
    T[j, i] = ( (k/(rho*Cp)) * (T[j-1, i+1] - 2.0*T[j-1, i] + T[j-1, i-1]) / dz**2 )  *  dt   +   T[j-1, i]

  if j % plot_every == 0:
    # Print and plot the depth vs temperature during this timestep

    # Also calculate an analytical solution
    T_analytical = analytical_tr(T_surf, T_ini, k/(rho*Cp), time, np.linspace(z[0], z[-1], 100))

    print("Temperatures at timestep " + str(j) + ":")
    print(T[j, 0:nz])
    plt.plot(T[j, 0:nz], -z, "o-", label="FD")   # minus sign is placed to make z axis point down
    if plot_analytical:
      plt.plot(T_analytical, -np.linspace(z[0], z[-1], 100), "-r", label="Analytical")
    plt.title("Time=" + str(time/(60*60*24*365.25*1e3)) + "kyrs")
    plt.xlabel("Temperature")
    plt.ylabel("Depth")
    plt.legend(loc=3)
    plt.show()


# Plot the temperature field as a function of time and location
SECINYR = 60*60*24*365.25
TIME, LOC = np.meshgrid(t, z, indexing="ij")
plt.contourf(TIME/(1000.0*SECINYR), LOC, T)
plt.xlabel("kyrs")
plt.ylabel("z")
plt.show()


