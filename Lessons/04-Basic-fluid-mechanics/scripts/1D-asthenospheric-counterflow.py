# -*- coding: utf-8 -*-
"""
1D-asthenospheric-counterflow.py

A script for plotting velocity magnitudes for 1D counterflow in the
asthenosphere.

dwhipp 01.16
"""

#--- User-defined input variables
hl = 100.0                                                                     # Thickness of lithosphere [km]
h = 200.0                                                                      # Thickness of asthenosphere [km]
u0 = 15.0                                                                      # Lithospheric plate velocity [cm/a]
numpts = 101                                                                   # Number of points to calculate velocity across channel
#--- End user-defined input

# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Convert inputs to SI values
h = h * 1000.0                                                                 # [km] -> [m]
hl = hl * 1000.0                                                               # [km] -> [m]
u0 = u0 / 1000.0 / 365.25 / 24.0 / 3600.0                                      # [mm/a] -> [m/s]

# Define channel arrays
y = np.linspace(0.0,h,numpts)
u = np.zeros(numpts)

# Loop across all values of y and define velocity
for i in range(numpts):
    # Insert equation for asthenospheric counterflow below
    u[i] = ????

# Rescale values of y and u for plotting
y = y / 1000.0
u = u * 1000.0 * 365.25 * 24.0 * 3600.0

# Create figure for plotting
plt.figure()

# Make plot
plt.plot(u,y,'ko-')

# Invert y axis
plt.gca().invert_yaxis()

# Add text label with thickness of lithospheric plate
plt.text(????)

# Label axes and add title
plt.xlabel("Flow velocity [mm/a]")
plt.ylabel("Distance across channel [km]")
plt.title("Asthenospheric counterflow")

# Show plot
plt.show()