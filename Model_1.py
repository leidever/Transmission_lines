#from __future__ import division

import matplotlib.pyplot as plt
import numpy as np

lightspeed = 300_000_000.0            # m|s
F_source = 10_000_000.0            # Hz
L_line = lightspeed / F_source       # meters

# Load, transmission (transformator unit), source (0)
Z_load = 75.0
Z_source = 50.0
Z_line = np.sqrt(Z_load*Z_source)     # Z_T


f = np.linspace(0.0, 2*F_source, 100)

phase = (2*np.pi*L_line/lightspeed)*f
#print("phase:", phase)

Z_in = Z_line * (Z_load + 1j*Z_line*np.tan(phase)) / (Z_load + 1j*Z_line*np.tan(phase))
#print("Z_in:", Z_in)

G = np.abs((Z_in - 1) / (Z_in + 1))
#print("G:", G)

SWR = (1 + G) / (1 - G)

fig, ax = plt.subplots()                        # будет 1 график, на нем:
ax.plot(f, G, color="blue", label="G")          # функция G, синий, надпись G
ax.plot(f, SWR, color="red", label="SWR")       # функция SWR, красный, надпись SWR
ax.set_xlabel("f")                              # подпись у горизонтальной оси x
ax.set_ylabel("G, SWR")                          # подпись у вертикальной оси y
ax.legend()                                      # показывать условные обозначения

plt.show()                                      # показать рисунок
