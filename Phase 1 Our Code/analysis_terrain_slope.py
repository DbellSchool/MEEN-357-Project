import numpy as np
from math import ceil, log
from numpy import sign
import sys
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar
from subfunctions import rover, F_net, get_gear_ratio, planet



terrain_angle = np.linspace(-10, 35, 25)

Crr = 0.2

L =-100
R = 100

Ng = get_gear_ratio(rover['wheel_assembly']['speed_reducer'])
r =rover['wheel_assembly']['wheel']['radius']
v_max = []


for i in terrain_angle:
    Fwrap = lambda x: F_net( x, [i], rover, planet, [0.2])
    w = root_scalar(Fwrap,method='bisect', bracket=[L,R])
    wWheel = w.root/Ng
    V = wWheel*r
    v_max.append(V)
    
print(v_max)  

plt.plot(v_max,terrain_angle, '-b')
plt.xlabel("omega [rad/s]")
plt.ylabel("Terrain Angle [degrees]")
plt.grid("on")
plt.show()
