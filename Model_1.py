#from __future__ import division

import matplotlib
import numpy as np

matplotlib.rcParams["axes.grid"] = True
matplotlib.rcParams["figure.figsize"] = 16,12

F_source = 10.0            # МHz
L_line = 7.5       # meters
betta = 20.96   # 1/meters

# Load, transmission (transformator unit), source (0)
Z_load = 75.0
Z_source = 50.0
Z_line = np.sqrt(Z_load*Z_source)     # Z_T

f = np.linspace(0.0, 2*F_source, 100)
G = np.zeros(100)

def calculate_G (f, koef):
    phase = koef*f
    Z_in = Z_line * (Z_load + 1j*Z_line*np.tan(phase)) / (Z_line + 1j*Z_load*np.tan(phase))
    G = np.abs((Z_in - Z_source) / (Z_in + Z_source))
    return G

fig, ax = plt.subplots()                # будет 1 график, на нем:
koef = 2*3.1415*L_line/299.8            # с учетом размерностей
G = calculate_G(f, koef)
ax.plot(f, G, color="blue", label="G")          # функция G, синий, надпись G


koef = 2*3.1415*L_line*1.1/299.8            # с учетом размерностей
G = calculate_G(f, koef)
ax.plot(f, G, color="red", linestyle='--', label="G при 1.1L")   # функция G, синий, надпись G

koef = 2*3.1415*L_line*1.05/299.8            # с учетом размерностей
G = calculate_G(f, koef)
ax.plot(f, G, color="red", linestyle='-.', label="G при 1.05L")

koef = 2*3.1415*L_line*0.95/299.8            # с учетом размерностей
G = calculate_G(f, koef)
ax.plot(f, G, color="red", linestyle='-.', label="G при .95L")

koef = 2*3.1415*L_line*0.9/299.8            # с учетом размерностей
G = calculate_G(f, koef)
ax.plot(f, G, color="red", linestyle='--', label="G при 0.9L")   # функция G, синий, надпись G




ax.set_xlabel("f, MHz")                              # подпись у горизонтальной оси x
ax.set_ylabel("G")                          # подпись у вертикальной оси y
ax.legend()                                      # показывать условные обозначения

plt.show()                                      # показать рисунок
