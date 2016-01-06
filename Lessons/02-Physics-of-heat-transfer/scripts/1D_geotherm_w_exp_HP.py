#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# 1D_geotherm_w_exp_HP.py
#
# This script plots a one-dimensional geotherm with heat production for an input
# thickness, heat production and basal heat flow. Heat production decreases
# exponentially with depth.
# Note: We're assuming T=0 at z=0 in this example.
#
# dwhipp 09.14

#--- User-defined input values ------------------------------------------------#
zmax=40.                                                                       # Thickness of the model [km]
T0=0.                                                                           # Surface temperature [deg. C]
qmax=20.                                                                        # Basal heat flow [mW m-2]
S1=2.5                                                                          # Heat production [µW m-3]
S2=2.5                                                                          # Heat production [µW m-3]
S3=2.5                                                                          # Heat production [µW m-3]
e1=5.                                                                           # e-folding depth [km]
e2=10.                                                                          # e-folding depth [km]
e3=20.                                                                          # e-folding depth [km]
k=2.75                                                                          # Thermal conductivity [W m-1 K-1]
numpts=101                                                                      # Number of points across zl for the calculation

#--- End user-defined input ---------------------------------------------------#

#q0=65.                                                                          # Surface heat flow [mW m-2]

#--- DO NOT MODIFY ANYTHING BELOW THIS LINE -----------------------------------#

# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Scale input values
zmax=zmax*1000.                                                                 # km -> m
#q0=q0/1000.                                                                     # mW m-2 -> W m-2
qmax=qmax/1000.                                                                 # mW m-2 -> W m-2
S1=S1/1.e6                                                                      # µW m-3 -> W m-3
S2=S2/1.e6                                                                      # µW m-3 -> W m-3
S3=S3/1.e6                                                                      # µW m-3 -> W m-3
e1=e1*1000.                                                                     # km -> m
e2=e2*1000.                                                                     # km -> m
e3=e3*1000.                                                                     # km -> m

# Parameter ranges
z=np.linspace(0,zmax,numpts);
T1=np.zeros(len(z))
T2=np.zeros(len(z))
T3=np.zeros(len(z))
T4=np.zeros(len(z))

# Temperature calculation
for i in range(len(z)):
    T1[i] = T0 + (qmax*z[i])/(k) + (S1*e1**2.)/(k)*(1-np.exp(-z[i]/e1))
    T2[i] = T0 + (qmax*z[i])/(k) + (S2*e2**2.)/(k)*(1-np.exp(-z[i]/e2))
    T3[i] = T0 + (qmax*z[i])/(k) + (S3*e3**2.)/(k)*(1-np.exp(-z[i]/e3))
    T4[i] = -(S1 * pow(z[i],2))/(2.*k) + (qmax + S1 * zmax)/k * z[i]

#T1 = T0 + (qmax*z)/(k) + (S1*e1**2.)/(k)*(1-np.exp(-z/e1))
#T2 = T0 + (qmax*z)/(k) + (S2*e2**2.)/(k)*(1-np.exp(-z/e2))
#T3 = T0 + (qmax*z)/(k) + (S2*e3**2.)/(k)*(1-np.exp(-z/e3))
#T1 = T0 + (qmax*z)/(k) + ((q0-qmax)*e1)/(k)*(1-np.exp(-z/e1))
#T2 = T0 + (qmax*z)/(k) + ((q0-qmax)*e2)/(k)*(1-np.exp(-z/e2))
#T3 = T0 + (qmax*z)/(k) + ((q0-qmax)*e3)/(k)*(1-np.exp(-z/e3))

# Scale for plotting
z=z/1000.
zmax=zmax/1000.

# Plot geotherm
plt.plot(T1,z,'k',lw=2,label='e-folding depth: '+str(e1/1000.)+' km')
plt.scatter(T1,z,s=8,color='k')
plt.plot(T2,z,'b',lw=2,label='e-folding depth: '+str(e2/1000.)+' km')
plt.scatter(T2,z,s=8,color='b')
plt.plot(T3,z,'r',lw=2,label='e-folding depth: '+str(e3/1000.)+' km')
plt.scatter(T3,z,s=8,color='r')
plt.plot(T4,z,'g',lw=2,label='constant concentration')
plt.scatter(T4,z,s=8,color='g')

plt.axis([0.0, max([max(T1),max(T2),max(T3),max(T4)]), 0.0, zmax])

plt.gca().invert_yaxis()

plt.xlabel('Temperature [$^\circ$C]')
plt.ylabel('Depth [km]')

plt.legend(loc=0)

plt.show()
