#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# 1D_geotherm_w_HP.py
#
# This script plots a one-dimensional geotherm with heat production for an input
# thickness, heat production and basal heat flow.
# Note: We're assuming T=0 at z=0 in this example.
#
# dwhipp 09.13

#--- User-defined input values ------------------------------------------------#
zmax=40.                                                                        # Thickness of the model [km]
qmax=20.                                                                        # Basal heat flow [mW m-2]
S1=0.0                                                                          # Heat production [µW m-3]
S2=0.5                                                                          # Heat production [µW m-3]
S3=1.0                                                                          # Heat production [µW m-3]
k=2.75                                                                          # Thermal conductivity [W m-1 K-1]
numpts=101                                                                      # Number of points across zl for the calculation

#--- End user-defined input ---------------------------------------------------#

#--- DO NOT MODIFY ANYTHING BELOW THIS LINE -----------------------------------#

# Import libraries
import pylab

# Scale input values
zmax=zmax*1000.                                                                 # km -> m
qmax=qmax/1000.                                                                 # mW m-2 -> W m-2
S1=S1/1.e6                                                                      # µW m-3 -> W m-3
S2=S2/1.e6                                                                      # µW m-3 -> W m-3
S3=S3/1.e6                                                                      # µW m-3 -> W m-3

# Parameter ranges
z=pylab.linspace(0,zmax,numpts);

# Temperature calculation
T1 = -(S1 * pow(z,2))/(2*k) + (qmax + S1 * zmax)/k * z
T2 = -(S2 * pow(z,2))/(2*k) + (qmax + S2 * zmax)/k * z
T3 = -(S3 * pow(z,2))/(2*k) + (qmax + S3 * zmax)/k * z

# Scale for plotting
z=z/1000.
zmax=zmax/1000.

# Plot geotherm
pylab.plot(T1,z,'k',lw=2,label=str(S1*1.e6)+' $\mu$W m$^{-3}$')
pylab.scatter(T1,z,s=8,color='k')

pylab.plot(T2,z,'b',lw=2,label=str(S2*1.e6)+' $\mu$W m$^{-3}$')
pylab.scatter(T2,z,s=8,color='b')

pylab.plot(T3,z,'r',lw=2,label=str(S3*1.e6)+' $\mu$W m$^{-3}$')
pylab.scatter(T3,z,s=8,color='r')

pylab.axis([0.0, max(T3), 0.0, zmax])

pylab.gca().invert_yaxis()

pylab.xlabel('Temperature [$^\circ$C]')
pylab.ylabel('Depth [km]')

pylab.legend()

pylab.show()
