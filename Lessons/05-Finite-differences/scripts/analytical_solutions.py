import numpy as np
import matplotlib.pyplot as plt
import math

def analytical_tr(T0, T1, kappa, t, z):
  z = np.array(z)  # to make sure it's an array

  T = np.zeros(z.size)

  for iz in range(z.size):
    T[iz] = math.erfc(z[iz] / (2.0 * (kappa * t)**0.5)) * (T0 - T1) + T1

  return T


def analytical_ss_qT(z, k, A, z1, q0, z2, T0):

  ### Calculate the analytical solution of the heat equation
  #    * Steady-state
  #    * No advection
  #    * Constant heat conductivity
  #    * Constant heat production
  #
  # Choosable Dirichlet + von Neumann boundary conditions
  #  T=T0 at z=z1
  #  q=q0 at z=z2
  
  # k:       heat conductivity, W/mK
  # A:       heat production rate, W/m^3
  # z1, q0:  location and value of boundary condition one (von neumann)
  # z2, T0:  location and value of boundary condition two (dirichlet)
  
  # Calculate integration constants
  Ca = q0 + A*z1
  Cb = -q0 * z2 - A*z1*z2 + k*T0 + 0.5*A*z2**2
  
  ### Evaluate temperature at chosen range
  T = (- 0.5 * A * z**2 + Ca*z + Cb) / k
  
  return T
