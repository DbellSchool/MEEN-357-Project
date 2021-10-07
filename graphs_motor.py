#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 12:47:17 2021

@author: laurenberryman
"""


import matplotlib.pyplot as plt
import numpy as np
from MEEN_357_Goup_Project_Lib import tau_dcmotor


# Create a python script that outputs a graph of the DC motor
# doesn't display anything to the console
# plots the following three graphs in a 3x1 array using matplot.lib
# graph 1 : motor shaft speed vs. motor shaft torque (x-axis = torque)
# graph 2: motor power vs. motor shaft torque (x-axis = torque)
# graph 3: motor power vs. motor shaft speed (x-axis = speed)
# label the axes of the graphs
# use the functions we created to generate the graphs



fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.tight_layout()




# graph 1 - torque vs. speed

x1 = np.linspace(0, 3.8, 25)
t = tau_dcmotor(x1)
ax1.plot(t, x1)
ax1.set_xlabel("motor shaft torque [Nm]")
ax1.set_ylabel("motor shaft speed [rad/s]")


# ax1.subtitle ("graph")


#ax1.plot(x1,y1)

# 2nd graph
P = t*x1
ax2.plot(t,P)
ax2.set_xlabel("motor shaft torque [Nm]")
ax2.set_ylabel("motor power [W]")


# 3rd graph
R = P*t
ax3.plot(x1, P)
ax3.set_xlabel("motor shaft speed [rad/s]")
ax3.set_ylabel("motor power [W]")

#plt.

plt.show()