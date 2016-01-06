#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# 1D_intrusion.py
#
# This script plots the cooling of a 1D intrusion with time
#
# dwhipp 09.13

#--- User-defined input values ------------------------------------------------#
Ti=700.                                                                         # Intrusion temperature [deg. C]
Tb=200.                                                                         # Background temperature [deg. C]
l=2.                                                                            # Intrusion width [km]
w=10.                                                                            # Model width [km]
kappa=1e-6                                                                      # Thermal diffusivity [m^2 s-1]
t1=10.                                                                          # Time 1 [a]
t2=100.                                                                         # Time 2 [a]
t3=1000.                                                                        # Time 3 [a]
t4=10000.                                                                       # Time 4 [a]
t5=100000.                                                                      # Time 5 [a]
t6=1000000.                                                                     # Time 6 [a]
numpts=101                                                                      # Number of points across w

#--- End user-defined input ---------------------------------------------------#

#--- DO NOT MODIFY ANYTHING BELOW THIS LINE -----------------------------------#

# Import libraries
import pylab,scipy,scipy.special

# Scale input values
l=l*1000.                                                                       # km -> m
w=w*1000.                                                                       # km -> m
t1=t1*365.25*24*3600
t2=t2*365.25*24*3600
t3=t3*365.25*24*3600
t4=t4*365.25*24*3600
t5=t5*365.25*24*3600
t6=t6*365.25*24*3600

# Parameter ranges
x=pylab.linspace(-w,w,numpts);

# Temperature calculation
T1=Tb+((Ti-Tb)/2)*(scipy.special.erf((0.5*l-x)/(scipy.sqrt(4*kappa*t1)))+scipy.special.erf((0.5*l+x)/(scipy.sqrt(4*kappa*t1))))
T2=Tb+((Ti-Tb)/2)*(scipy.special.erf((0.5*l-x)/(scipy.sqrt(4*kappa*t2)))+scipy.special.erf((0.5*l+x)/(scipy.sqrt(4*kappa*t2))))
T3=Tb+((Ti-Tb)/2)*(scipy.special.erf((0.5*l-x)/(scipy.sqrt(4*kappa*t3)))+scipy.special.erf((0.5*l+x)/(scipy.sqrt(4*kappa*t3))))
T4=Tb+((Ti-Tb)/2)*(scipy.special.erf((0.5*l-x)/(scipy.sqrt(4*kappa*t4)))+scipy.special.erf((0.5*l+x)/(scipy.sqrt(4*kappa*t4))))
T5=Tb+((Ti-Tb)/2)*(scipy.special.erf((0.5*l-x)/(scipy.sqrt(4*kappa*t5)))+scipy.special.erf((0.5*l+x)/(scipy.sqrt(4*kappa*t5))))
T6=Tb+((Ti-Tb)/2)*(scipy.special.erf((0.5*l-x)/(scipy.sqrt(4*kappa*t6)))+scipy.special.erf((0.5*l+x)/(scipy.sqrt(4*kappa*t6))))

# Rescale for plotting
x=x/1000.
w=w/1000.
l=l/1000.
t1=t1/(365.25*24*3600)
t2=t2/(365.25*24*3600)
t3=t3/(365.25*24*3600)/1000.0
t4=t4/(365.25*24*3600)/1000.0
t5=t5/(365.25*24*3600)/1000.0
t6=t6/(365.25*24*3600)/1000000.0

# Initial intrusion geometry
xgeom=pylab.array([-w,0.-l/2.,0.-l/2.,0.+l/2.,0.+l/2.,w])
Tgeom=pylab.array([Tb,Tb,Ti,Ti,Tb,Tb])

# Plot geotherm
pylab.plot(xgeom,Tgeom,linewidth=2,color='black')
pylab.plot(x,T1,'black',label=str(t1)+' a',lw=2)
pylab.scatter(x,T1,s=8,color='black')
pylab.plot(x,T2,'red',label=str(t2)+' a',lw=2)
pylab.scatter(x,T2,s=8,color='red')
pylab.plot(x,T3,'blue',label=str(t3)+' ka',lw=2)
pylab.scatter(x,T3,s=8,color='blue')
pylab.plot(x,T4,'green',label=str(t4)+' ka',lw=2)
pylab.scatter(x,T4,s=8,color='green')
pylab.plot(x,T5,'purple',label=str(t5)+' ka',lw=2)
pylab.scatter(x,T5,s=8,color='purple')
pylab.plot(x,T6,'gray',label=str(t6)+' Ma',lw=2)
pylab.scatter(x,T6,s=8,color='gray')

pylab.axis([-w, w, Tb-50., Ti+50.])

pylab.text(780,5,'1D geotherm with advection',color='k')
pylab.xlabel('Width [km]')
pylab.ylabel('Temperature [$^\circ$C]')

pylab.legend()

pylab.show()
