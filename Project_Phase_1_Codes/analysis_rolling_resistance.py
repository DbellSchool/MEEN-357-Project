"""###########################################################################
#   This script solves and plots the maximum rover speed at various rolling  
#   resistance values for Phase 1 of the TAMU MEEN 357 project
#
#   Created by: Jonathan Weaver-Rosen
#   Last Modified: 24 June 2021
###########################################################################"""

import numpy as np
from subfunctions import *
from define_rovers import *
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

rover, planet = define_rover_1()
terrain_angle = 0
Crr_list = np.linspace(0.01,0.4,25)
omega_max = np.zeros(len(Crr_list), dtype = float)
omega_nl = rover['wheel_assembly']['motor']['speed_noload']

# find where F_net == 0
for ii in range(len(Crr_list)):
    fun = lambda omega: F_net(omega, terrain_angle, rover, planet, float(Crr_list[ii]))
    sol = root_scalar(fun, method='bisect', bracket=[0, omega_nl]) # note that this value is the max MOTOR shaft speed
    omega_max[ii] = sol.root
    
# translate into rover velocity
Ng = get_gear_ratio(rover['wheel_assembly']['speed_reducer'])
r = rover['wheel_assembly']['wheel']['radius']
omega_output = omega_max/Ng 

v_max = r*omega_output

# Plot
plt.plot(Crr_list, v_max)
plt.xlabel('Coefficient of Rolling Resistance [-]')
plt.ylabel('Max Rover Speed [m/s]')