"""###########################################################################
#   This script graphs motor characteristics for Phase 1 of the TAMU 
#   MEEN 357 project
#
#   Created by: Jonathan Weaver-Rosen
#   Last Modified: 24 June 2021
###########################################################################"""

import matplotlib.pyplot as plt
import numpy as np
from define_rovers import *
from subfunctions import tau_dcmotor

rover, planet = define_rover_1()

# generate motor shaft speeds
omega_nl = rover['wheel_assembly']['motor']['speed_noload']
omega = np.linspace(0,omega_nl)

# calculate motor shaft torque
tau = tau_dcmotor(omega, rover['wheel_assembly']['motor'])
# r = rover['wheel_assembly']['wheel']['radius']
# v_motor = [r*x for x in omega]

# Calculate power
P = tau*omega


# Plots
f, axs = plt.subplots(3,1,figsize=(10,10))

plt.subplot(3,1,1)
plt.plot(tau, omega)
plt.xlabel('Motor Shaft Torque [Nm]')
plt.ylabel('Motor Shaft Speed [rad/s]')

plt.subplot(3,1,2)
plt.plot(tau, P)
plt.xlabel('Motor Shaft Torque [Nm]')
plt.ylabel('Motor Power [W]')

plt.subplot(3,1,3)
plt.plot(omega, P)
plt.xlabel('Motor Shaft Speed [rad/s]')
plt.ylabel('Motor Power [W]')

plt.show()