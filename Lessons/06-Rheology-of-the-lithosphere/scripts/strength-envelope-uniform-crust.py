'''
strength-envelope-uniform-crust.py

This script can be used for plotting strength envelopes for a lithosphere with
a uniform crust. The script includes a function sstemp() that can be used for
calculating the lithospheric temperature as a function of the input material
properties

dwhipp 01.16 (modified from code written by L. Kaislaniemi)
'''

# --- USER INPUT PARAMETERS ---
# Model geometry
z_surf = 0.0                                                                   # Elevation of upper surface [km]
z_bott = 100.0                                                                 # Elevation of bottom boundary [km]
nz = 100                                                                       # Number of grid points

# Boundary conditions
T_surf = 0.0                                                                   # Temperature of the upper surface [deg C]
q_surf = 65.0                                                                  # Surface heat flow [mW/m^2]

# Thermal conductivity (constant across model thickness)
k = 2.75                                                                        # Thermal conductivity [W/m K]

# Deformation rate
edot = 1.0e-15                                                                 # Reference strain rate [1/s]

# Constants
g = 9.81                                                                       # Gravitational acceleration [m/s^2]
R = 8.314                                                                      # Gas constant

# Layer depths
L1 = 35.0                                                                      # Depth to base of layer one [km]

# MATERIAL PROPERTY DEFINITIONS
# Crust (Wet quartzite - Gleason and Tullis, 1995)
mat1 = 'Wet quartzite'
A1 = 1.1                                                                       # Average heat production rate for crust [uW/m^3]
rho1 = 2800.0                                                                  # Rock density [kg/m^3]
Avisc1 = 1.1e-4                                                                # Viscosity constant [MPa^-n s^-1]
Q1 = 223.0                                                                     # Activation energy [kJ/mol]
n1 = 4.0                                                                       # Power-law exponent
mu1 = 0.85                                                                     # Friction coefficient
C1 = 0.0                                                                       # Cohesion [MPa]

# Mantle (Wet olivine - Hirth and Kohlstedt, 1996)
mat2 = 'Wet olivine'
A2 = 0.02                                                                      # Heat production rate for mantle [uW/m^3]
rho2 = 3300.0                                                                  # Rock density [kg/m^3]
Avisc2 = 4.876e6                                                               # Viscosity constant [MPa^-n s^-1]
Q2 = 515.0                                                                     # Activation energy [kJ/mol]
n2 = 3.5                                                                       # Power-law exponent
mu2 = 0.6                                                                      # Friction coefficient
C2 = 60.0                                                                      # Cohesion [MPa]

# END MATERIAL PROPERTY DEFINITIONS
# --- END USER INPUTS ---

# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Define function to calculate temperatures (DO NOT MODIFY)
def sstemp(A,k,dz,nz,T_surf,q_surf):
    # Generate an empty array for temperature values
    T = np.zeros(nz)

    # Set boundary conditions
    # the upper surface temperature and the temperature at one grid point below
    T[0] = T_surf

    ## Grid point one needs special handling as T[-1] is not available
    # Calculate "ghost point" outside the model domain, where grid point -1 
    # would be, assuming surface heat flow q_surf
    Tghost = T[0] - q_surf * dz / k  # = "T[-1]"
    # Use the same finite difference formula to calculate T as for 
    # the inner points, but replace "T[-1]" by ghost point value
    T[1] = -A[1] * dz**2 / k - Tghost + 2*T[0]

    # Calculate temperatures across specified thickness
    for i in range(2, nz):                                                     # NB! Grid points 0 and 1 omitted as they cannot be calculated
        T[i] = -A[i] * dz**2 / k - T[i-2] + 2*T[i-1]
    return T

# Define conversion factors
km2m = 1.0e3                                                                   # [km] to [m]
mW2W = 1.0e-3                                                                  # [mW] to [W]
uW2W = 1.0e-6                                                                  # [uW] to [W]
MPa2Pa = 1.0e6                                                                 # [MPa] to [Pa]
kJ2J = 1.0e3                                                                   # [kJ] to [J]

# Convert material property units to SI
z_surf = z_surf * km2m
z_bott = z_bott * km2m
q_surf = q_surf * mW2W
A1 = A1 * uW2W
A2 = A2 * uW2W
L1 = L1 * km2m
Avisc1 = Avisc1 / MPa2Pa**n1
Avisc2 = Avisc2 / MPa2Pa**n2
Q1 = Q1 * kJ2J
Q2 = Q2 * kJ2J
C1 = C1 * MPa2Pa
C2 = C2 * MPa2Pa

# Generate the grid
# Regular grid is used, so that in FD calculations
# only dz is needed. Array z is used only for plotting.
dz = (z_bott - z_surf) / (nz - 1)
z = np.linspace(z_surf, z_bott, nz)

# Generate the material properties arrays
A = np.zeros(nz)
rho = np.zeros(nz)
Avisc = np.zeros(nz)
Q = np.zeros(nz)
n = np.zeros(nz)
mu = np.zeros(nz)
C = np.zeros(nz)

for i in range(nz):
    # Fill material property arrays for depths in the crust
    if ????:
        A[i] = A1
        rho[i] = rho1
        Avisc[i] = Avisc1
        Q[i] = Q1
        n[i] = n1
        mu[i] = mu1
        C[i] = C1
    # Fill material property arrays for depths in the mantle
    else:
        A[i] = A2
        rho[i] = rho2
        Avisc[i] = Avisc2
        Q[i] = Q2
        n[i] = n2
        mu[i] = mu2
        C[i] = C2

# Call function to get temperatures
T = sstemp(A,k,dz,nz,T_surf,q_surf)
T = T + 273.15                                                                 # Convert to Kelvins

# Initialize arrays
P = np.zeros(nz)
frict = np.zeros(nz)
visc = np.zeros(nz)
strength = np.zeros(nz)

# Calculate lithostatic pressure
for i in range(1, nz):
    P[i] = P[i-1] + rho[i] * g * dz

# Loop over all points and calculate frictional and viscous strengths
for i in range(nz):
    # Calculate frictional shear strength using Coulomb criterion
    frict[i] = ????
    # Calculate viscous strength using Dorn's law
    visc[i] = ????
    # Use logical statements to make sure the stored strength value is the
    # smaller of the two calculated above for each point
    if ????:
        strength[i] = ????
    else:
        strength[i] = ????

# Rescale values for plotting
T = T - 273.15
z = z / km2m
strength = strength / MPa2Pa
z_bott = z_bott / km2m

# Create figure window for plot
plt.figure()

# PLOT #1 - Left panel, temperature versus depth
plt.subplot(121)

# Plot temperature on left subplot
plt.plot(T, z, "ro-")

# Invert y axis
plt.gca().invert_yaxis()

# Label axes
plt.xlabel("Temperature [$^{\circ}$C]")
plt.ylabel("Depth [km]")

# PLOT #2 - Right panel, strength versus depth
plt.subplot(122)

# Plot strength versus deprh
plt.plot(strength, z, "ko-")   # minus sign is placed to make z axis point down

# Invert y axis
plt.gca().invert_yaxis()

# Label axes
plt.xlabel("Strength [MPa]")

# Add text labels for materials
plt.text(0.2*max(strength), 0.8*z_bott, "Layer 1: "+mat1)
plt.text(0.2*max(strength), 0.85*z_bott, "Layer 2: "+mat2)

plt.show()
