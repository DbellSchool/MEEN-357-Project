#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 22:24:05 2021

@author: laurenberryman
"""
# graphs_sr

# speed, torque, and power of the SPEED REDUCER OUTPUT SHAFT

import matplotlib.pyplot as plt
import numpy as np
from subfunctions import tau_dcmotor, get_gear_ratio, wheel_assembly

# call Ng from previous function and dictionary
Ng = get_gear_ratio(wheel_assembly['speed_reducer'])

fig, (ax1, ax2, ax3) = plt.subplots(3) # sets up fig
fig.tight_layout() #changes lay out to make neet

# Graph 1 - speed reducer torque vs. speed
t_sr = []
x1_sr = np.linspace(0, 3.8, 25) # list of 25 numbers form 0-3.8

for i in range(len(x1_sr)):
    t_sr.append(tau_dcmotor(x1_sr[i]/Ng))
ax1.plot(t_sr, x1_sr)

ax1.set_xlabel("SR torque [Nm]") # SR refers to the speed reducer output shaft
ax1.set_ylabel("SR speed [rad/s]")


# Graph 2 - speed reducer torque vs. power

P_sr = []
for i in range(len(x1_sr)):
    #pass
    #print(type(t_sr[i][0]),type(x1_sr[i]))
    P_sr.append(t_sr[i][0] * x1_sr[i])
ax2.plot(t_sr, P_sr)
ax2.set_xlabel("SR torque [Nm]")
ax2.set_ylabel("SR power [W]")

#Graph 3 - speed reducer speed vs. power
ax3.plot(x1_sr, P_sr)
ax3.set_xlabel("SR speed [rad/s]")
ax3.set_ylabel("SR power [W]")

plt.show()