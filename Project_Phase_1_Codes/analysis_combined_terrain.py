"""###########################################################################
#   This script solves and plots the maximum rover speed at various terrain 
#   angles AND rolling resistance values for Phase 1 of the TAMU MEEN 357 
#   project
#
#   Created by: Jonathan Weaver-Rosen
#   Last Modified: 24 June 2021
###########################################################################"""

import numpy as np
from subfunctions import *
from define_rovers import *
# from numerical_methods import bisection_root_finder, secant_root_finder
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, axes3d

rover, planet = define_rover_1()
Crr_list = np.linspace(0.01,0.4,25)
slope_list_deg = np.linspace(-10,35,25)
N = len(Crr_list)

# grid every combination
Crr_mat, slope_mat = np.meshgrid(Crr_list,slope_list_deg)

omega_max = np.zeros(np.shape(Crr_mat), dtype = float)
omega_nl = rover['wheel_assembly']['motor']['speed_noload']

# find where F_net == 0
for ii in range(N):
    for jj in range(N):
        fun = lambda omega: F_net(omega, float(slope_list_deg[ii]), rover, planet, float(Crr_list[jj]))
        try:
            sol = root_scalar(fun, method='bisect', bracket=[0, omega_nl])
            if (sol.root <= omega_nl) and (sol.root >= 0) :
                omega_max[ii,jj] = sol.root  # note that this value is the max MOTOR shaft speed
            else:
                raise Exception('Omega outside of feasible range. Assigning NaN...')
        except:
            try:
                sol = root_scalar(fun, method='secant', x0=0, x1=omega_nl)
                if (sol.root <= omega_nl) and (sol.root >= 0) :
                    omega_max[ii,jj] = sol.root  # note that this value is the max MOTOR shaft speed
                else:
                    raise Exception('Omega outside of feasible range. Assigning NaN...')
            except:
                omega_max[ii,jj] = np.nan
            
# translate into rover velocity
Ng = get_gear_ratio(rover['wheel_assembly']['speed_reducer'])
r = rover['wheel_assembly']['wheel']['radius']
omega_output = omega_max/Ng 

v_max = r*omega_output

# Plot
figure = plt.figure(figsize=(7,7))
ax = Axes3D(figure, elev=20, azim=50)

ax.plot_surface(Crr_mat, slope_mat, v_max)
ax.set_xlabel('Coefficient of Rolling Resistance [-]')
ax.set_ylabel('Terrain Angle [deg]')
ax.set_zlabel('Max Rover Speed [m/s]')