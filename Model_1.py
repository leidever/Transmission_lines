#from __future__ import division

import matplotlib.pyplot as plt
import numpy as np

SPEED_OF_LIGHT = 3.0E8
SOURCE_FREQUENCY = 10.0E6

# gamma = alpha + j*beta - propagation constant
alpha = 0
def beta(f):
    beta=(2*np.pi/SPEED_OF_LIGHT)*f
    return beta

# Load, transmission (transformator unit), source (0)
Z_L = 75.0
Z_0 = 50.0
Z_T = np.sqrt(Z_0*Z_L)

# Voltage reflection coefficient
def G (Z_L, Z_0):
    G  = (Z_L - Z_0) / (Z_L + Z_0)
    return G

# SWR
def SWR(G):
    SWR = (1 + G) / (1 - G)
    return SWR

N = 10
F_min = 0.0
F_max = 30.0E6
delta = (F_max - F_min)/N
x = [None] * (N)

for i in range(N):
    x[i] = F_min + delta*(i+1)
    print (beta(x[i]))
    

print (x)



# All losses are zero, use tan instead of tanh
def Z_in(l):
    Z_in = Z_T*((Z_L - 1j*Z_T*np.tan(beta*l))/(Z_T-1j*Z_L*np.tan(beta*l)))
    return abs(Z_in)


N = 100
x = np.linspace(0.0, l_0, N)

y = Z_in(x)

fig = plt.figure()
plt.plot(x, y, label = "Zin")
plt.xlabel('l, meters')
plt.ylabel('Z_in, Ohm')

plt.legend()
plt.grid(True)

plt.show()