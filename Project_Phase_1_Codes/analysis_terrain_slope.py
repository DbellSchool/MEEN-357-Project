"""###########################################################################
#   This script solves and plots the maximum rover speed at various terrain 
#   angles for Phase 1 of the TAMU MEEN 357 project
#
#   Created by: Jonathan Weaver-Rosen
#   Last Modified: 24 June 2021
###########################################################################"""

import numpy as np
from subfunctions import *
from define_rovers import *
# from numerical_methods import bisection_root_finder
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

rover, planet = define_rover_1()
Crr = 0.2
slope_list_deg = np.linspace(-10,35,25)
omega_max = np.zeros(len(slope_list_deg), dtype = float)
omega_nl = rover['wheel_assembly']['motor']['speed_noload']

# find where F_net == 0
for ii in range(len(slope_list_deg)):
    fun = lambda omega: F_net(omega, float(slope_list_deg[ii]), rover, planet, Crr)
    # omega_max[ii], fval, n_iter = bisection_root_finder(fun, 0, omega_nl) # note that this value is the max MOTOR shaft speed
    sol = root_scalar(fun, method='bisect', bracket=[0, omega_nl])
    omega_max[ii] = sol.root
    
# translate into rover velocity
Ng = get_gear_ratio(rover['wheel_assembly']['speed_reducer'])
r = rover['wheel_assembly']['wheel']['radius']
omega_output = omega_max/Ng 

v_max = r*omega_output

# Plot
plt.plot(slope_list_deg, v_max)
plt.xlabel('Terrain Angle [deg]')
plt.ylabel('Max Rover Speed [m/s]')

plt.show()