#from __future__ import division

import matplotlib.pyplot as plt
import numpy as np

F_source = 10.0            # МHz
L_line = 7.5       # meters
betta = 20.96   # 1/meters

# Load, transmission (transformator unit), source (0)
Z_load = 75.0
Z_source = 50.0
Z_line = np.sqrt(Z_load*Z_source)     # Z_T

l = np.linspace(1.0, 15.0, 100)
#print (f)

koef =2*3.1415*10E6/2.998E8

phase = koef*l
#print("phase:", phase)

Z_in = Z_line * (Z_load + 1j*Z_line*np.tan(phase)) / (Z_line + 1j*Z_load*np.tan(phase))
#print("Z_in:", Z_in)

G = np.abs((Z_in - Z_source) / (Z_in + Z_source))
#print("G:", G)

SWR = np.abs((1 + G) / (1 - G))

fig, ax = plt.subplots()                        # будет 1 график, на нем:
ax.plot(f, G, color="blue", label="G")          # функция G, синий, надпись G
ax.plot(f, SWR, color="red", label="SWR")       # функция SWR, красный, надпись SWR
ax.set_xlabel("l, m")                              # подпись у горизонтальной оси x
ax.set_ylabel("G, SWR")                          # подпись у вертикальной оси y
ax.legend()                                      # показывать условные обозначения

plt.show()                                      # показать рисунок
