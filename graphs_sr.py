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
from MEEN_357_Goup_Project_Lib import tau_dcmotor, get_gear_ratio, wheel_assembly

# call Ng from previous function and dictionary
Ng = get_gear_ratio(wheel_assembly['speed_reducer'])

fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.tight_layout()

# graph 1 - speed reducer torque vs. speed
t_sr = []
x1_sr = np.linspace(0, 3.8, 25)
for i in range(len(x1_sr)):
    t_sr.append(tau_dcmotor(x1_sr[i]/Ng))
ax1.plot(t_sr, x1_sr)
ax1.set_xlabel("SR torque [Nm]") # SR refers to the speed reducer output shaft
ax1.set_ylabel("SR speed [rad/s]")


# graph 2 - speed reducer torque vs. power
# HAVE NO IDEA HOW TO DO THIS

# TRIAL 2 - same wonky graphs
#P_sr = []
#for i in range(len(t_sr)):
   # P_sr.append(t_sr[i] * x1_sr)
P_sr = t_sr * x1_sr
ax2.plot(t_sr, P_sr)
ax2.set_xlabel("SR torque [Nm]")
ax2.set_ylabel("SR power [W]")
    






#for i in range(x1_sr):
    #for j in range(t_sr):
       # P_sr.append(t_sr[j] * x1_sr[i])

#for i in range(len(t_sr)):
    #P_sr.append(t_sr[i] * x1_sr)
    


#P_sr = t_sr * x1_sr



# TRIAL 1 - produced the same wonky graphs
#Psr = []
#for i in t_sr:
   # for j in Psr:
      #  Psr = t_sr * x1_sr
       # Psr.append(P_sr)
    




#for h in range(len(t_sr)):
    #for i in range(len(x1_sr)):
        #t_sr.append(tau_dcmotor(x1_sr[i]/Ng))
        
        
ax2.plot(t_sr, P_sr)
ax2.set_xlabel("SR torque [Nm]")
ax2.set_ylabel("SR power [W]")
    






#t_sr * x1_sr


ax2.plot(t_sr, P_sr)


# graph 3 - speed reducer speed vs. power
ax3.plot(x1_sr, P_sr)
ax3.set_xlabel("SR speed [rad/s]")
ax3.set_ylabel("SR power [W]")









#Ng = get_gear_ratio(x1_sr)

#x1_sr = np.linspace(0, 3.8, 25)/Ng

#t_sr = tau_dcmotor(x1_sr)
#ax1.plot(t_sr, x1_sr)


