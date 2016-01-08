import numpy as np
import matplotlib.pyplot as plt



z_surf = 0.0  # location of upper surface
z_bott = 50e3 # location of bottom boundary

nz = 11        # number of grid points
nt = 8        # number of timesteps to calculate
dt = 6250000000000.0 # timestep to use, in seconds

T_surf = 0.0   # temperature of the upper surface
T_bott = 600.0 # temperature of the lower boundary

k = 2.5        # heat conductivity
rho = 2800     # density
Cp = 850       # heat capacity

plot_every = 1   # plot the temperature field every Nth timestep



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
j = 0 # i.e. initial time step
T[j, 0] = T_surf             # time step zero, grid point zero, T=T_surf
T[j, nz-1] = T_bott          # time step zero, last grid point, T=T_bott
for i in range(1, nz-1):     
  T[j, i] = 0.0              # time step zero, grid point i, T=0

time = 0  # Variable to calculate the model time in the time loop

# Loop over time steps, skipping the first one (=initial condition)
for j in range(1,nt):
  time = time + dt
  
  # Set boundary condition
  ???? # set the required boundary conditions for this time step

  # Calculate temperature at inner grid points
  ????

  if j % plot_every == 0:
    # Print and plot the depth vs temperature during this timestep
    print("Temperatures at timestep " + str(j) + ":")
    print(T[j, 0:nz])
    plt.plot(T[j, 0:nz], -z, "o-")   # minus sign is placed to make z axis point down
    plt.title("Time=" + str(time/(60*60*24*365.25*1e3)) + "kyrs")
    plt.xlabel("Temperature")
    plt.ylabel("Depth")
    plt.show()


# Plot the temperature field as a function of time and location
SECINYR = 60*60*24*365.25
TIME, LOC = np.meshgrid(t, z, indexing="ij")
plt.contourf(TIME/(1000.0*SECINYR), LOC, T)
plt.xlabel("kyrs")
plt.ylabel("z")
plt.show()


