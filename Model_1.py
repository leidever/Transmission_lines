#from __future__ import division

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 16})

# speed of light, source frequency and wave length
с = 3.0E8; f = 10.0E6; l_0 = с/f;

# gamma = alpha + j*beta - propagation constant
alpha = 0
beta=2*np.pi/l_0

# Load, transmission (transformator unit), source (0)
Z_L = 75.0
Z_0 = 50.0
Z_T = np.sqrt(Z_0*Z_L)


#def gamma(x):
#    gamma = (Z_T*Z_L-Z_0*Z_T + 1j*(Z_T*Z_T-Z_0*Z_L)/np.tan(x)) / (Z_T*Z_L+Z_0*Z_T + 1j*(Z_T*Z_T+Z_0*Z_L)/np.tan(x))
#    return abs(gamma)

# All losses are zero, use tan instead of tanh
def Z_in(l):
    Z_in = Z_T*((Z_L - 1j*Z_T*np.tan(beta*l))/(Z_T-1j*Z_L*np.tan(beta*l)))
    return abs(Z_in)

'''
def gamma(x):
    gamma = (Z_in(x) - Z_0) / (Z_in(x) + Z_0)
    return abs(gamma)
'''

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