from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from define_edl_system import *
from subfunctions_EDL import *
from define_planet import *
from define_mission_events import *


#######
# *************************************
# load dicts that define the EDL system (includes rover), planet,
# mission events and so forth.


tmax = 2000   # [s] maximum simulated time


# 14 to 19 meters at 0.5  for parahoto diamater
D_vals = np.arange(14,19.5,0.5,dtype= float)

time = np.zeros(len(D_vals))
v = np.zeros(len(D_vals))
Success = np.zeros(len(D_vals))



for i in range(len(D_vals)):
    edl_system = define_edl_system_1()
    mars = define_planet()
    mission_events = define_mission_events()


    # Overrides what might be in the loaded data to establish our desired
    # initial conditions
    edl_system['altitude'] = 11000  # [m] initial altitude
    edl_system['velocity'] = -578     # [m/s] initial velocity
    edl_system['parachute']['deployed'] = True   # our parachute is open
    edl_system['parachute']['ejected'] = False   # and still attached
    edl_system['sky_crane']["on"]  = False # skycrane off
    edl_system["speed_control"]['on']= False # Speed controler Off
    edl_system["position_control"]['on'] = False# position controler Off
    edl_system['rover']['on_ground'] = False # the rover has not yet landed
    edl_system['parachute']['diameter'] = D_vals[i]

    [t, Y, edl_system] = simulate_edl(edl_system, mars, mission_events, tmax, True)
    time[i] = t[-1]
    v[i] = Y[1][-1]
    #update_edl_state()
    if ( edl_system["rover"]["on_ground"] == True
            and abs(edl_system["sky_crane"]["danger_speed"]) >= abs(Y[0][-1])
            and edl_system['sky_crane']["danger_altitude"] <= abs(Y[1][-1])): # Safe landing conditions 

        Success[i] =  1
    else :
        Success[i] = 0 

    ### 1 
    ############################




plot1 = plt.figure(0)
plot1.tight_layout(pad=10.0)

#lt.subplots( )
fig, axs = plt.subplots(3,1, sharex=True) 
fig.tight_layout(pad=3.0)
axs[0].plot(D_vals, time)
axs[0].set_title('Time vs. parachute diameter')
axs[0].grid()
axs[0].set_ylabel('[s]')
axs[1].plot(D_vals,v)
axs[1].set_title('Rover speed at simulation termination vs. parachute diameter')
axs[1].grid()
axs[1].set_ylabel('[m/s]')
axs[2].plot(D_vals,Success)
axs[2].set_title('Rover landing success vs. parachute diameter')
axs[2].grid()
axs[2].set_ylabel('[-]')

plt.show()