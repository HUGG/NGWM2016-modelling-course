import numpy as np
import matplotlib.pyplot as plt
import math

N = 1000
z = np.linspace(0, 3, N)
erfvals = np.zeros(N)
erfcvals = np.zeros(N)

for iz in range(N):
  erfvals[iz] = math.erf(z[iz])
  erfcvals[iz] = math.erfc(z[iz])

plt.plot(z, erfvals, "r-", label="erf")
plt.plot(z, erfcvals, "b-", label="erfc")
plt.legend()
plt.title("Error function values")
plt.show()
