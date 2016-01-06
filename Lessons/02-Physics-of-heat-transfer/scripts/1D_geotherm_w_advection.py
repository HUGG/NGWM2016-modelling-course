#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# 1D_geotherm_w_advection.py
#
# This script plots a one-dimensional geotherm with advection for an input set
# of lithospheric thicknesses, lithosphere-asthenosphere boundary temperatures,
# thermal diffusivities and advection velocities.
# Note: We're assuming T=0 at z=0 in this example.
#
# dwhipp 09.13

#--- User-defined input values ------------------------------------------------#
zl=100                                                                          # Thickness of the lithosphere [km]
Tl=1300                                                                         # Temperature of the LAB [degrees C]
kappa=1e-6                                                                      # Thermal diffusivity [m^2 s-1]
u1=0.000001                                                                     # Advection velocity 1 [mm/a]
u2=0.1                                                                          # Advection velocity 2 [mm/a]
u3=1.0                                                                          # Advection velocity 3 [mm/a]
u4=5.                                                                           # Advection velocity 4 [mm/a]
u5=-0.1                                                                         # Advection velocity 5 [mm/a]
u6=-1.                                                                          # Advection velocity 6 [mm/a]
u7=-5.                                                                          # Advection velocity 7 [mm/a]
numpts=101                                                                      # Number of points across zl for the calculation

#--- End user-defined input ---------------------------------------------------#

#--- DO NOT MODIFY ANYTHING BELOW THIS LINE -----------------------------------#

# Import libraries
import pylab

# Scale input values
zl=zl*1000                                                                      # km -> m
u1=u1*1e-3/(365.25*24.*3600.)                                                   # mm/a -> m/s
u2=u2*1e-3/(365.25*24.*3600.)                                                   # mm/a -> m/s
u3=u3*1e-3/(365.25*24.*3600.)                                                   # mm/a -> m/s
u4=u4*1e-3/(365.25*24.*3600.)                                                   # mm/a -> m/s
u5=u5*1e-3/(365.25*24.*3600.)                                                   # mm/a -> m/s
u6=u6*1e-3/(365.25*24.*3600.)                                                   # mm/a -> m/s
u7=u7*1e-3/(365.25*24.*3600.)                                                   # mm/a -> m/s

# Parameter ranges
z=pylab.linspace(0,zl,numpts);

# Temperature calculation
T1=Tl*(1-pylab.exp(-u1*z/kappa))/(1-pylab.exp(-u1*zl/kappa))
T2=Tl*(1-pylab.exp(-u2*z/kappa))/(1-pylab.exp(-u2*zl/kappa))
T3=Tl*(1-pylab.exp(-u3*z/kappa))/(1-pylab.exp(-u3*zl/kappa))
T4=Tl*(1-pylab.exp(-u4*z/kappa))/(1-pylab.exp(-u4*zl/kappa))
T5=Tl*(1-pylab.exp(-u5*z/kappa))/(1-pylab.exp(-u5*zl/kappa))
T6=Tl*(1-pylab.exp(-u6*z/kappa))/(1-pylab.exp(-u6*zl/kappa))
T7=Tl*(1-pylab.exp(-u7*z/kappa))/(1-pylab.exp(-u7*zl/kappa))

# Rescale for plotting
z=z/1000.
zl=zl/1000.

# Plot geotherm
pylab.plot(T1,z,'k')
pylab.scatter(T1,z,s=8,color='k')
pylab.plot(T2,z,'r')
pylab.scatter(T2,z,s=8,color='r')
pylab.plot(T3,z,'r')
pylab.scatter(T3,z,s=8,color='r')
pylab.plot(T4,z,'r')
pylab.scatter(T4,z,s=8,color='r')
pylab.plot(T5,z,'b')
pylab.scatter(T5,z,s=8,color='b')
pylab.plot(T6,z,'b')
pylab.scatter(T6,z,s=8,color='b')
pylab.plot(T7,z,'b')
pylab.scatter(T7,z,s=8,color='b')

pylab.axis([0.0, Tl, 0.0, zl])

pylab.gca().invert_yaxis()

pylab.text(780,5,'1D geotherm with advection',color='k')
pylab.xlabel('Temperature [$^\circ$C]')
pylab.ylabel('Depth [km]')

pylab.show()
