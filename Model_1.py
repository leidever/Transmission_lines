'''from cmath import sqrt'''
from __future__ import division

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 16})


Z_L = 75.00
Z_T = 61.24
Z_0 = 50.00

#def gamma(x):
#    gamma = (Z_T*Z_L-Z_0*Z_T + 1j*(Z_T*Z_T-Z_0*Z_L)/np.tan(x)) / (Z_T*Z_L+Z_0*Z_T + 1j*(Z_T*Z_T+Z_0*Z_L)/np.tan(x))
#    return abs(gamma)

def Z_in(x):
    Z_in = Z_T*((Z_L - 1j*Z_T*np.tanh(x))/(Z_T-1j*Z_L*np.tanh(x)))
    return Z_in


def gamma(x):
    gamma = (Z_in(x) - Z_0) / (Z_in(x) + Z_0)
    return abs(gamma)



N = 100
x = np.linspace(-10.0, 10., N)

y = gamma(x)

fig = plt.figure()
plt.plot(x, y, label = "gamma")
#plt.xlabel('epsilon')
#plt.ylabel('Г (коэф. отражения)')

plt.legend()
plt.grid(True)

plt.show()


