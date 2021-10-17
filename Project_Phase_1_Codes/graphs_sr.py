"""###########################################################################
#   This script graphs output shaft characteristics for Phase 1 of the TAMU 
#   MEEN 357 project
#
#   Created by: Jonathan Weaver-Rosen
#   Last Modified: 24 June 2021
###########################################################################"""

import matplotlib.pyplot as plt
import numpy as np
from define_rovers import *
from subfunctions import tau_dcmotor, get_gear_ratio

rover, planet = define_rover_1()

Ng = get_gear_ratio(rover['wheel_assembly']['speed_reducer'])

# generate output shaft speeds
omega_nl = rover['wheel_assembly']['motor']['speed_noload']
omega_motor = np.linspace(0,omega_nl)
omega_output = omega_motor/Ng

# calculate output shaft torque
tau_motor = tau_dcmotor(omega_motor, rover['wheel_assembly']['motor'])
tau_output = Ng*tau_motor

# Calculate power
P_output = tau_output*omega_output


# Plots
f, axs = plt.subplots(3,1,figsize=(10,10))

plt.subplot(3,1,1)
plt.plot(tau_output, omega_output)
plt.xlabel('SR Output Shaft Torque [Nm]')
plt.ylabel('SR Output Shaft Speed [rad/s]')

plt.subplot(3,1,2)
plt.plot(tau_output, P_output)
plt.xlabel('SR Output Shaft Torque [Nm]')
plt.ylabel('SR Output Power [W]')

plt.subplot(3,1,3)
plt.plot(omega_output, P_output)
plt.xlabel('SR Output Shaft Speed [rad/s]')
plt.ylabel('SR Output Power [W]')