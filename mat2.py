import numpy as np
import matplotlib.pyplot as plt

N = 7
OECD = (242, 244, 255, 263, 269, 276, 285)
NonOECD = (282, 328, 375, 417, 460, 501, 535)
Sum = ('524', '572', '630', '680', '729', '777', '820')
ind = np.arange(N)
width = 0.5

p1 = plt.bar(ind, NonOECD, width, color = 'r')
p2 = plt.bar(ind, OECD, width, color = 'b', bottom = NonOECD)

plt.ylabel('Quadrillion Btu')
plt.title('World Total Energy Consumption 2010 - 2040')
plt.xticks(ind+width/2, ('2010', '2015', '2020', '2025', '2030', '2035', '2040'))
plt.yticks(np.arange(0, 1001, 200))
plt.legend((p1[0], p2[0]), ('Non - OECD', 'OECD'), loc = 2, frameon = 'false')
plt.tick_params(top = 'off', bottom = 'off', right = 'off')
plt.grid(axis = 'y', linestyle = '-')

plt.show()