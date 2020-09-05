#from __future__ import division

import matplotlib.pyplot as plt
import numpy as np

#plt.rcParams["figure.figsize"] = 16,12

F_source = 10.0            # МHz
L_line = 7.5       # meters
betta = 20.96   # 1/meters

# Load, transmission (transformator unit), source (0)
Z_load = 75.0
Z_source = 50.0
Z_line = np.sqrt(Z_load*Z_source)     # Z_T

f = np.linspace(0.0, 2*F_source, 1000)


def calculate_G (f, koef):
    phase = koef*f
    Z_in = Z_line * (Z_load - 1j*Z_line*np.tan(phase)) / (Z_line - 1j*Z_load*np.tan(phase))
    G = np.abs((Z_in - Z_source) / (Z_in + Z_source))
    return G

fig, ax = plt.subplots()                # будет 1 график, на нем:

koef = 2*3.1415*L_line/299.8            # с учетом размерностей
G = calculate_G(f, koef)
SWR = np.abs((1 + G) / (1 - G))

#ax.plot(f, G, color="blue", label="G")          # функция G, синий, надпись G
ax.plot(f, SWR, color="red", label="SWR")       # функция SWR, красный, надпись SWR

f = np.linspace(1, F_source, 1000)

koef = 2*3.1415*(L_line+29.98/8)/299.8        # увеличили на четверть длины волны
G = calculate_G(f, koef)
SWR = np.abs((1 + G) / (1 - G))
#ax.plot(f, G, color="red", linestyle='--', label="G при ")   # функция G, синий, надпись G
ax.plot(f, SWR, color="black", linestyle='--', label="SWR при увеличении на 1/8 дл. волны")       # функция SWR, красный, надпись SWR

koef = 2*3.1415*(L_line+29.98/16)/299.8            # с учетом размерностей
G = calculate_G(f, koef)
SWR = np.abs((1 + G) / (1 - G))
#ax.plot(f, G, color="red", linestyle='-.', label="G при 1.05L")
ax.plot(f, SWR, color="black", linestyle='-.', label="SWR при увеличении на 1/16 дл. волны")       # функция SWR, красный, надпись SWR
#
#koef = 2*3.1415*L_line*0.95/299.8            # с учетом размерностей
#G = calculate_G(f, koef)
#ax.plot(f, G, color="red", linestyle='-.', label="G при .95L")
#
#koef = 2*3.1415*L_line*0.9/299.8            # с учетом размерностей
#G = calculate_G(f, koef)
#ax.plot(f, G, color="red", linestyle='--', label="G при 0.9L")   # функция G, синий, надпись G
#



ax.set_xlabel("f, MHz")                              # подпись у горизонтальной оси x
#ax.set_ylabel("G")                          # подпись у вертикальной оси y
ax.set_ylabel("SWE")                          # подпись у вертикальной оси y
ax.legend()                                      # показывать условные обозначения
ax.grid("on")
plt.figure(figsize=(18, 16), dpi= 80, facecolor='w', edgecolor='k')
plt.show()                                      # показать рисунок
