#from __future__ import division

import matplotlib.pyplot as plt
import numpy as np

SPEED_OF_LIGHT = 3.0E8
GENERATOR_FREQUENCY = 10.0E6
LINE_LENGTH = 7.5

# Load, transmission (transformator unit), source (0)
Z_L = 75.0
Z_0 = 50.0
Z_T = np.sqrt(Z_0*Z_L)

N = 1000;

F_min = 0.0; F_max = 20.0E6; dF = (F_max - F_min)/N

F = [None] * (N); G = [None] * (N); SWR = [None] * (N)

def Z_in(Z_L, Z_0, phase):
    Z_in = Z_0 * (Z_L - 1j*Z_0*np.tan(phase)) / (Z_0 - 1j*Z_L*np.tan(phase))
    return Z_in

for i in range(N):
    F[i] = F_min + dF*(i+1)
    phase = 2*np.pi/SPEED_OF_LIGHT*LINE_LENGTH*F[i]
    Z =  abs(Z_in(Z_L, Z_T, phase)) 
    G[i]= (Z - Z_0) / (Z + Z_0)
    SWR[i] = (1 + G[i]) / (1 - G[i])

fig = plt.figure()
plt.plot(F, SWR, label = "SWR")

plt.xlabel('F, Hz')
plt.ylabel('SWR')

plt.legend()
plt.grid(True)

plt.show()