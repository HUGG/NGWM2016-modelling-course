#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# e-folding_of_HP.py
#
# This script plots exponentially decreasing concentrations of heat-producting
# elements for given input concentrations and e-folding depths.
#
# dwhipp 01.16

#--- User-defined input values ------------------------------------------------#
zmax=40.                                                                        # Thickness of the model [km]
S=2.5                                                                           # Heat production [uW m-3]
z_efold1=5.0                                                                    # e-folding depth [km]
z_efold2=10.0                                                                   # e-folding depth [km]
z_efold3=20.0                                                                   # e-folding depth [km]
numpts=101                                                                      # Number of points across zmax for the calculation

#--- End user-defined input ---------------------------------------------------#

#--- DO NOT MODIFY ANYTHING BELOW THIS LINE -----------------------------------#

# Import libraries
import pylab

# Parameter ranges
z=pylab.linspace(0,zmax,numpts);
S4=pylab.linspace(S,S,numpts)

# Concentration calculations
S1=S/pylab.exp(z/z_efold1)
S2=S/pylab.exp(z/z_efold2)
S3=S/pylab.exp(z/z_efold3)

# Plot geotherm
pylab.plot(S1,z,'k',lw=2,label=str(z_efold1)+' km')
pylab.scatter(S1,z,s=8,color='k')

pylab.plot(S2,z,'b',lw=2,label=str(z_efold2)+' km')
pylab.scatter(S2,z,s=8,color='b')

pylab.plot(S3,z,'r',lw=2,label=str(z_efold3)+' km')
pylab.scatter(S3,z,s=8,color='r')

pylab.plot(S4,z,'g',lw=2,label='constant')
pylab.scatter(S4,z,s=8,color='g')

pylab.axis([0.0, 1.05*S, 0.0, zmax])

pylab.gca().invert_yaxis()

pylab.xlabel('Volumetric heat production [$\mu W m^{-3}$]')
pylab.ylabel('Depth [km]')

pylab.legend(loc=4)

pylab.show()
