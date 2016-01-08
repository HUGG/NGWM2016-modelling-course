# -*- coding: utf-8 -*-
"""
1D-channel-flow.py

A script for plotting velocity magnitudes across a 1D channel subject to a
pressure gradient and/or with one channel wall moving at a constant velocity.

dwhipp 01.16
"""

#--- User-defined input variables
h = 10.0                                                                       # Channel width [km]
eta = 1.0e21                                                                   # Channel fluid viscosity [Pa s]
dpdx = 0.0                                                                     # Channel pressure gradient [Pa] (should be negative)
u0 = 0.0                                                                       # Channel wall velocity [mm/a]
numpts = 101                                                                   # Number of points to calculate velocity across channel
#--- End user-defined input

# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Convert inputs to SI values
h = h * 1000.0                                                                 # [km] -> [m]
u0 = u0 / 1000.0 / 365.25 / 24.0 / 3600.0                                      # [mm/a] -> [m/s]

# Define channel arrays
y = np.linspace(0.0,h,numpts)
u = np.zeros(numpts)

# Loop across all values of y and define velocity
for i in range(numpts):
    # Insert equation for 1D channel flow below
    u[i] = ????

# Rescale values of y and u for plotting
y = y / 1000.0
u = u * 1000.0 * 365.25 * 24.0 * 3600.0

# Create figure for plotting
plt.figure()

# Make plot
plt.plot(u,y)

# Invert y axis
plt.gca().invert_yaxis()

# Label axes and add title
plt.xlabel("Flow velocity [mm/a]")
plt.ylabel("Distance across channel [km]")
plt.title("1D channel flow")

# Show plot
plt.show()